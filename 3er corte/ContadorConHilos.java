import javax.naming.InterruptedNamingException;

public class ContadorConHilos {
    
    static int counter = 0;

    public static void main(String[] args)
    {
        final int SIM_THREADS = 4;
        final int ITERATIONS = 10000;

        System.out.println("Inicio (secuencial). Esperando resultado... ");

        Thread[] threads = new Thread[SIM_THREADS];

        for(int t = 0; t < SIM_THREADS; t++)
        {
            final int id = t;

            //2 parametros: funcion a ejecutar
            threads[t] = new Thread(
                () -> 
                {
                    for(int i = 0; i< ITERATIONS; i++);
                    {
                        counter++;
                        try {
                            Thread.sleep(1); // Simula trabajo
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }, // funcion lambda a ejecutar por cada hilo
                "Thread id:"+t+1            
            );
            System.out.printf("creado hilo %d: estado %s ",threads[t].getName(), threads[t].getState());

        }

        for(int t = 0; t < SIM_THREADS; t++)
        {
            threads[t].start();
             System.out.printf("iniciado hilo %d: estado %s, IsAlive:%b ",threads[t].getName(), threads[t].getState(), threads[t].isAlive());
        }

        //interrumpimos hilo principal:
        //entra en estado TIMED_WAITING:
        try{
            Thread.sleep(50); // al interrumpirse, cede el uso de la CPU a los demas hilos.
        } catch(InterruptedException e){
            // Todo Auto generated catch block
            e.printStackTrace();
        }

         //esperar que todos los hilos terminen:
         for (int i = 0; i < NUM_HILOS; i++) {
            try {
                //join hace que ele hilo actual espere hasta que ele hilo i termine
                threads[i].join(); // SOMETER LA EJECUCION Y LA FINALIZACION DE CADA HILO AL HILO PRINCIPAL:
                System.out.printf("%s ha terminado (isAlive=%b, estado=%s)%n",
                        threads[i].getName(), threads[i].isAlive(), threads[i].getState());
                { catch (InterruptedNamingException e) {
                        e.printStackTrace();    
                }
            }
         

    }
}
    