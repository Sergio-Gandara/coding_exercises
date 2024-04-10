
using System;


namespace MyNameSpace{
    public class MyClass{
        public static void Main(string[] args){
            Console.WriteLine("Hello World!");
            Console.Write("What is your name? :");
            string name = Console.ReadLine();
            Console.WriteLine("And hello " + name + " !, It is a pleasure to meet you!");
            Console.WriteLine("Current date is: " + DateTime.Now);
        }
    }
}


