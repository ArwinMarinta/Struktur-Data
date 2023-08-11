package Tugas1;

public class Queue<E> {
    private SinglyLinkedList<E> list = new SinglyLinkedList<>();

    public Queue() {
    }

    public int size() {
        return list.size();
    }

    public boolean isEmpty() {
        return list.isEmpty();
    }

    public void enqueue(E element) {
        list.addLast(element);
    }

    public E dequeue() {
        return list.removeFirst();
    }

    public E first() {
        return list.first();
    }
}
