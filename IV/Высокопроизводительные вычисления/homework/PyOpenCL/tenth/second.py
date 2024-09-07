import numpy as np
import pyopencl as cl

platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
context = cl.Context([device])
queue = cl.CommandQueue(context)

limit_Nmax = 1e7  # Макс точек
limit_a = 1e6  # Макс радиус круга
Pi = 0.0

a = 100  # радиус круга

while a < limit_a:
    Nmax = a
    while Nmax <= limit_Nmax:
        num_points = int(Nmax)

        random_x = np.random.rand(num_points).astype(np.float32)
        random_y = np.random.rand(num_points).astype(np.float32)
        count = np.zeros(1).astype(np.int32)

        buffer = cl.mem_flags
        random_x_buf = cl.Buffer(context, buffer.READ_ONLY | buffer.COPY_HOST_PTR, hostbuf=random_x)
        random_y_buf = cl.Buffer(context, buffer.READ_ONLY | buffer.COPY_HOST_PTR, hostbuf=random_y)
        count_buf = cl.Buffer(context, buffer.READ_WRITE | buffer.COPY_HOST_PTR, hostbuf=count)

        kernel_code = """
            __kernel void monte_carlo(
                const int num_points,
                __global const float* random_x,
                __global const float* random_y,
                __global int* count)
            {
                int i = get_global_id(0);
                if (i >= num_points)
                    return;

                float x = random_x[i];
                float y = random_y[i];
                if (x * x + y * y <= 1.0f)
                    atomic_add(count, 1);
            }
            """

        program = cl.Program(context, kernel_code).build()
        monte_carlo_kernel = program.monte_carlo
        monte_carlo_kernel.set_args(np.int32(num_points), random_x_buf, random_y_buf, count_buf)

        global_size = (num_points,)
        cl.enqueue_nd_range_kernel(queue, monte_carlo_kernel, global_size, None).wait()

        cl.enqueue_copy(queue, count, count_buf).wait()

        Nmax *= 2
    a *= 2
Pi = 4.0 * count[0] / num_points
print(f"Pi: {Pi}")
