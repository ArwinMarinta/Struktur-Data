package Tugas1;

public class main {
    public static void main(String[] args) {
        SinglyLinkedList<String> MyList = new SinglyLinkedList<String>();

        // // Menambahkan Element baru ke belakang

        MyList.addFirst("3");
        MyList.addFirst("4");
        // //
        // //// Menambahkan Element baru ke Depan
        // //
        MyList.addLast("3");
        MyList.addLast("4");

        MyList.reverseList();
        MyList.removeElement("");
        while (!MyList.isEmpty()) {
            MyList.removeFirst();
        }

        // Stack dan Queue

        Queue<String> myQueue = new Queue<String>();
        Stack<String> myStack = new Stack<String>();
        String myTestString = myStack.reverse("FALSA");

    }

}