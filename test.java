public class test {
 
    public static void main(String[] args) {
     
    for(int n=1;n<=50;n++) {
    System.out.println(Fibonacci(n));
    }
     
    }
     
    public static int Fibonacci(int n) {
    if(n==1||n==2) {
    return 1;
    }
    else {
    return Fibonacci(n-2)+Fibonacci(n-1);
    }
    }
}