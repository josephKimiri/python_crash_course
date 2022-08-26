//save file as Calculator.java and run in cmd/any IDE  
import javax.swing.*; //note we use "javax" for "JFrame" 
import java.awt.event.*; 
 
class Operation(){ 
   public void calc(){ 
      JFrame frame1 = new JFrame("Calculator"); //frame_name("label") 
      frame1.setBounds(300,200,220,350); //(x_crd,y_crd,width,height) 
 
      JButton a = new JButton ("1"); //button_name("label") 
      a.setBounds(10,220,50,50); //(x_crd,y_crd,width,height) 
      frame1.add(a); 
 
      frame1.setVisible(true);  
 
      a.addActionListener(new ActionListener(){ 
         public void actionPerformed (ActionEvent ae){ 
            //code for JButton a 
	    //use wrapper classes for operations 
            //Float.parseFloat("str") 
         }  
      }); 
   } 
} 
class Calculator(){ 
   public static void main(String args[]){ 
      new Operation.calc();  
      }  
} 