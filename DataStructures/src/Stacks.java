public class Stacks {
    public static final int MAX = 100;
    int [] array = new int[100];
    static int top = -1;
    public boolean isEmpty(int[] array){
        if (top < 0)
            return true;
        return false;
    }
    public  void push(int n){
        if (top >= MAX) {
            System.out.println("The stack is either empty or full");
            return;
        }
        else {
            array[++top] = n;
            System.out.println("Element added");
            return;
        }
    }
    public void pop(){
        if (isEmpty(array)){
            System.out.println("The stack is empty");
            return;
        }
        System.out.println("Element "+array[top]+" popped");
        top--;

    }
    public void display(){
        if (isEmpty(array)){
            System.out.println("The stack is empty");
            return;
        }
        for (int i = 0; i <=top; i++){
            System.out.print(array[i]);
        }
        System.out.println();
    }
    public static void main(String[] args){
        Stacks stack = new Stacks();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.display();
        stack.pop();
        stack.display();
    }
}
