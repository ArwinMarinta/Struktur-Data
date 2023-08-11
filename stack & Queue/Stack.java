package Tugas1;

public class Stack<E> {
    private final SinglyLinkedList<E> list = new SinglyLinkedList<>();
    public Stack(){}
    public int size(){
        return list.size();
    }
    public boolean isEmpty(){
        return list.isEmpty();
    }
    public void push(E element){
        list.addFirst(element);
    }
    public E pop(){
        return list.removeFirst();
    }
    public E top(){
        return list.first();
    }
    public String reverse(String myString) {
        System.out.println("Kalimat = " + myString);
        String newString = "";
        Stack<String> myStack = new Stack<>();
        for(int i = 0; i < myString.length(); i++){
            myStack.push(myString.substring(i, i+1));
        }
        while(!myStack.isEmpty()){
            newString += myStack.pop();
        }
        System.out.println("Kalimat Akhirnya = " + newString);
        return newString;
    }
}
