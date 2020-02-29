public class For{
    public static void main(String []args){
        int i;
        for(i=0;i<10;i++){
            System.out.println("i:" + i);
        }
        System.out.println("after roop i:" + i);
        System.out.println("Not 9");
        System.out.println("iに+1をした後で条件分岐を行うため、forを抜けた後のiはi<10の10になる");
    }
}