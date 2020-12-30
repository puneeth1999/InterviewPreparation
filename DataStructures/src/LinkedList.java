public class LinkedList{
    Node head;
    class Node{
        int data;
        Node next;
        Node(int data){
            this.data = data;
            this.next = null;
        }
    }
    public void insertLast(int d){
        Node current  = head;
        Node newNode = new Node(d);
        newNode.next = null;
        if (head == null){
            head = newNode;
            head.next = null;
        }else{
            while (current.next != null){
                current = current.next;
            }
            current.next = newNode;
        }
    }

    //NOT WORKING PROPERLY
    public void insertAtIndex(int data, int idx){
        int count = 0;
        Node current = head;
        Node newNode = new Node(data);
        if (head == null){
            System.out.println("The LinkedList is empty.");
            insertLast(data);
        }
        current = head;
        while (current.next != null){
            current = current.next;
        }
        if (count < idx) {
            System.out.println("The linkedList is not that long. Returning..");
            return;
        }
        count = 0;
        current = head;
        while (count <= idx){
            current = current.next;
            count += 1;
        }
        current.next = newNode;
    }
    public void showList(){
        Node current = head;
        while (current != null) {
            System.out.print(current.data);
            current = current.next;
        }
    }

    public static void main(String[] args) {
        LinkedList ll = new LinkedList();
        ll.insertLast(1);
        ll.insertLast(2);
        ll.insertLast(3);
        ll.insertAtIndex(4, 3);
        ll.showList();
    }
}
