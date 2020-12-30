public class Queues {
    public static final int MAX = 9999;
    int[] array = new int[MAX];
    int front = 0; int rear = 0;
    public void enqueue(int data){
        array[rear] = data;
        rear++;
        System.out.println("enqueued: "+data);
    }
    public void dequeue(){
        int temp = array[0];
        for (int i = 0; i < array.length - 1; i++){
            array[i] = array[i + 1];
        }
        rear--;
        System.out.println("Dequeued: "+temp);
    }
    public void display(){
        for(int i = 0; i<rear; i++)
            System.out.print(array[i]);
        System.out.println();
    }

    public static void main(String[] args){
        Queues queue = new Queues();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        queue.enqueue(4);
        queue.display();
        queue.dequeue();
        queue.display();
    }
}
