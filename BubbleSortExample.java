package LatihanPrakTugas1;
public class BubbleSortExample {
    static void bubbleSort(int[] arr) {
        int n = arr.length;
        int temp = 0;
        for(int i=0; i < n; i++){
            for(int j=1; j < (n-i); j++){
                if(arr[j-1] > arr[j]){
                    // elemen swap
                    temp = arr[j-1];
                    arr[j-1] = arr[j];
                    arr[j] = temp;
                }

            }
        }

    }
    public static void main(String[] args) {
        int arr[] ={0,-1,1,-2,2,-3,3,-4,4,-5};

//sorting array menggunakan bubble sort
        System.out.println("sebelum bubble sort");
        for(int i=0; i < arr.length; i++){
            if(i == (arr.length - 1)){
                System.out.print(arr[i]);
            } else {
                System.out.print(arr[i] + ",");
            }
        }
        System.out.println();

        bubbleSort(arr);

        System.out.println("sesudah bubble sort");
        for(int i=0; i < arr.length; i++){
            if(i == (arr.length - 1)){
                System.out.print(arr[i]);
            } else {
                System.out.print(arr[i] + ",");
            }
        }

    }
}

