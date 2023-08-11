class Node<T> {
    private T value;
    private Node<T> next;
    public Node(T value){
        this.value = value;
    }
    public void setNext(Node<T> next){
        this.next = next;
    }
    public Node<T> getNext(){
        return this.next;
    }
    public T getValue(){
        return this.value;
    }
    public String toString(){
        return String.valueOf(value);
    }
}

class LinkedList<T>{
    private Node<T> first;
    public int length;
    public LinkedList(){
    }
    public void add(T value){
        Node<T> temp = new Node<T>(value);
            if (this.first == null){
            this.first = temp;
            }
            else{
                this.getLast().setNext(temp);
            }
        length++;
    }
    public void remove(int index){
        Node<T> tempnode = this.get(index-1);
        Node<T> temp = tempnode.getNext();
        tempnode.setNext(temp.getNext());
        length--;
    }
    public void insert(T value,int index){
        Node<T> tempNode = this.get(index-1);
        Node<T> temp = tempNode.getNext();
        tempNode.setNext(new Node<T>(value));
        tempNode = tempNode.getNext();
        tempNode.setNext(temp);
        length++;
    }
    public void swap(int index1,int index2){
        Node<T> tempNode1 = this.get(index1);
        Node<T> tempNode2 = this.get(index2);
        this.remove(index1);
        this.insert(tempNode2.getValue(),index1);
        this.remove(index2);
        this.insert(tempNode1.getValue(),index2);
    }
    public Node<T> get(int index){
        Node<T> temp = first;
        for (int i=0;i<index;i++){
        temp = temp.getNext();
        }
        return temp;
    }
    public Node<T> getLast(){
        Node<T> last = first;
        while (last.getNext() != null){
            last = last.getNext();
        }
        return last;
    }
    @Override
    public String toString(){
        if (first == null){
            return null;
        }
        else{
            Node<T> temp = first;
            String str = temp.toString();
            while (temp.getNext() != null){
                temp = temp.getNext();
                str = str + temp.toString();
            }
            return str;
        }
    }
}

class Stack<T>{
    private Node<T> first;
    public Stack(){
    }
    public boolean hasPop(){
        return first != null;
    }
    public void push(T value){
        Node<T> temp = new Node<T>(value);
        if (first == null){
            first = temp;
        }
        else{
            temp.setNext(first);
            first = temp;
        }
    }
    public T pop(){
        if (this.hasPop()){
            Node<T> temp = first;
            first = first.getNext();
            return temp.getValue();
        }
        else {
            return null;
        }
    }
    public Node<T> getLast(){
        Node<T> temp = first;
        while(temp.getNext()!= null){
            temp = temp.getNext();
        }
        return temp;
    }
    @Override
    public String toString(){
        Node<T> temp = first;
        if (temp==null){
            return null;
        }
        else{
            String str = temp.toString();
            while (temp.getNext() !=null){
                temp = temp.getNext();
                str = str + temp.toString();
            }
            return str;
        }    
    }
}

class Queue<T>{
    public Node<T> first;
    public int length = 0;
    public Queue(){
    }
    public void push(T value){
        Node<T> temp = new Node<T>(value);
        if (first == null){
            this.first = temp;
        }
        else{
            Node<T> last = this.getLast();
            last.setNext(temp);
        }
        length++;
    }
    public Node<T> pop(){
        Node<T> temp = first;
        this.first = this.first.getNext();
        return temp;
    }
    public Node<T> getLast(){
        Node<T> temp = first;
        while(temp.getNext()!= null){
            temp = temp.getNext();
        }
        return temp;
    }
    @Override
    public String toString(){
        Node<T> temp = first;
        if (temp == null){
            return null;
        }
        else {
            String str = temp.toString();
            while (temp.getNext()!= null){
                temp = temp.getNext();
                str = str + temp.toString();
            }
            return str;
        }
    }
}
