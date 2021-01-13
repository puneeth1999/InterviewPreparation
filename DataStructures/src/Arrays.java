public class Arrays {
    int count;
    //Constructors
    //Create arrays of a specific size
    int [] array;
    public Arrays(int len){
        this.array = new int [len];
    }
    //Create arrays without any size given (OverLoading)
    public Arrays(){
        int len = 1;
        this.array = new int [len];
    }

    //Get the length of the array
    int getLength(){
        return count;
    }

    //Print the items in the array
    void printArray(){
        for (int i = 0; i < count; i++){
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }

    //Insert at the very end of the array
    void insert(int data){
        //If the count == array.length, then create a new array double the size and copy everything
        if (count == array.length){
            int[] new_array = new int[2 * count];
            for (int i = 0; i < array.length; i++){
                new_array[i] = array[i];
            }
            array = new_array;
        }
        array[count++] = data;
    }

    //Insert at a position
    void insert(int pos, int data){
        //Copy everything to it's right pos and insert then insert.
        //But before that, check if the array is full. i.e., check if count == array.length
        if (count == array.length){
            int[] new_array = new int[2*count];
            for (int i = 0; i < array.length; i++){
                new_array[i] = array[i];
            }
            array = new_array;
            array[count++] = data;
        }
        for (int i = pos; i < count; i++){
            array[++i] = array[i];
        }
        array[pos] = data;
    }

    //Pop
    //Pop in the front
    void pop(){
        if (count < array.length/2){
//            int [] new_arra
        }
    }

    public static void main(String[] args){
        Arrays a = new Arrays(3);
        a.insert(1);
        a.insert(2);
        a.insert(3);
        a.insert(4);
        a.printArray();
        a.insert(0, 0);
        a.insert(a.getLength()-1, 7);
        a.insert(2, 6);
        a.printArray();
        System.out.println(a.getLength());
    }
}
