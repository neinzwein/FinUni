import numpy as np
import pyopencl as cl
import matplotlib.pyplot as plt

max_iters=256
w,h = 720,480
xmin, xmax=-2,2
ymin, ymax=-2,2

kernel_code = """
__kernel void burning_ship(
    const int Nmax,
    __global float *res,
    __global float *xx,
    __global float *yy)
{
    int gid = get_global_id(0);
    float x = 0.0f;
    float y = 0.0f;
    float cx = xx[gid];
    float cy = yy[gid];
    int ii = 0;

    while (Nmax > ii && x * x + y * y < 4.0f){
        float x_new = fabs(x * x - y * y - cx);
        y = 2.0f * fabs(x * y) - cy;
        x = x_new;
        ii++;
    }
    res[gid] = ii;
}
"""

platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
context = cl.Context([device])
queue = cl.CommandQueue(context)

program = cl.Program(context, kernel_code).build()
burning_ship_kernel = program.burning_ship

x = np.linspace(xmin, xmax, w).astype(np.float32)
y = np.linspace(ymin, ymax, h).astype(np.float32)
x, y = np.meshgrid(x, y)
x = x.flatten()
y = y.flatten()

x_buf = cl.Buffer(context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=x)
y_buf = cl.Buffer(context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=y)
res_buf = cl.Buffer(context, cl.mem_flags.WRITE_ONLY, x.nbytes)

res = np.empty_like(x, dtype=np.int32)

burning_ship_kernel.set_args(np.int32(max_iters), res_buf, x_buf, y_buf)
cl.enqueue_nd_range_kernel(queue, burning_ship_kernel, (x.size,), None).wait()

cl.enqueue_copy(queue, res, res_buf).wait()

res = res.reshape((h, w))
plt.imshow(res, extent=(xmin, xmax, ymin, ymax), cmap='inferno')
plt.colorbar()
plt.title("Множество Горящего корабля (Burning Ship Fractal)")
plt.show()