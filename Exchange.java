/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package exchange;
import java.util.Scanner;
        
/**
 *
 * @author ibrahimrahimi
 */
public class Exchange {
 
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scanOBJ= new Scanner (System.in);
        
        System.out.println("please enter the currency in hand: ");
         String inHandCurrency=scanOBJ.next();
         System.out.println("please enter the currency required: ");
        String requiredCurrency=scanOBJ.next();
        
        System.out.println("please enter amount: ");
        double totalAmount=scanOBJ.nextDouble();
        
        System.out.println("please enter exchange rate:");
        double exchangeRate=scanOBJ.nextDouble();
        
        double exchangeAmount= totalAmount*exchangeRate;
       System.out.println("Total exchange amount: " + exchangeAmount );
       
        
        
        // TODO code application logic here
    }
    
}
