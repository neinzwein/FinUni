import pyopencl as cl
import numpy as np

t0 = 0.0  # начальное время
y0 = 1.0  # начальное значение y
h = 0.01  # шаг интегрирования
num_steps = 1000  # количество шагов

platform = cl.get_platforms()[0] #[0]GPU[1]CPU
device = platform.get_devices()[0] #I have 1
context = cl.Context([device])
queue = cl.CommandQueue(context)

y = np.zeros(num_steps + 1).astype(np.float32)
y[0] = y0

buffer = cl.mem_flags
buffer_y = cl.Buffer(context, buffer.READ_WRITE | buffer.COPY_HOST_PTR, hostbuf=y)

#( \frac{dy}{dt} = -2y ) Рунге-кутта
kernel_code = """
__kernel void Runga_Kutta(
    __global float* y, //Как я понял идет в буфер
    const int num_steps,
    const float t0,
    const float h)
{
    float k1,k2,k3,k4; // К - Клинское
    float yi = y[0];
    float t = t0;
    
    for (int i=0;i<num_steps;++i)
    {
        k1 = h * (-2.0f*yi);
        k2 = h * (-2.0f *(yi + k1/2.0f));
        k3 = h * (-2.0f *(yi + k2/2.0f));
        k4 = h * (-2.0f * (yi+k3));

        yi=yi + (k1+2.0f*k2+2.0f*k3+k4)/6.0f;
        y[i+1] = yi;
        t = t+h;
    }
}
"""

program = cl.Program(context,kernel_code).build()
Runge_Kutta_kernel = program.Runga_Kutta
Runge_Kutta_kernel.set_args(buffer_y,np.int32(num_steps),np.float32(t0),np.float32(h))

global_size=(num_steps,)
cl.enqueue_nd_range_kernel(queue,Runge_Kutta_kernel,global_size,None).wait()

cl.enqueue_copy(queue,y,buffer_y).wait()

print("Результс интегрейшн бай рунге-кутта метод:")
for i in range(10):
    print(f"y({t0+i*h}) = {y[i]}")