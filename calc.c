#include <stdio.h>
int choise;

void timestables(){
    int table = 0;
    int amount = 0;
    printf("enter the times table you want\n");
    scanf("%d", &table);
    for (size_t i = 0; i < 12; i++)
    {   
        amount = table * i;
        printf("%d * %d = %d\n",table , i , amount);
    }
    
    
}

void vat(){
    float vatamount;
    printf("Enter the amount for vat to be added\n ");
    scanf("%f", &vatamount);
    vatamount = vatamount + vatamount*0.2;
    printf("Your product with vat added is %f\n", vatamount);
    
    
}

void tax(){
    float taxamount;
    float income;
    printf("Enter the amount your income is\n ");
    scanf("%f", &income);
    if (income <= 12570)
    {
        printf("you pay no tax");
    }else if (income >= 12571 && income < 50270)
    {
        taxamount = income * 0.2;
        printf("you need to pay %f amount of tax.\n", taxamount);
    }
    else if (income >= 50271 && income < 150000)
    {
        taxamount = income * 0.4;
        printf("you need to pay %f amount of tax.\n", taxamount);
    }
    else if (income >= 150000 )
    {
        taxamount = income * 0.45;
        printf("you need to pay %f amount of tax.\n", taxamount);
    }
    
    
    
   
    
    
}


int main(){
    while (1)
    {
        printf("press 1 for times tables\n");
        printf("press 2 for vat calc\n");
        printf("press 3 for taxs calc\n");
        scanf("%d", &choise);
        if (choise == 1)
        {
            timestables();

        }else if (choise == 2)
        {
            vat();
        }
        else if (choise == 3)
        {
            tax();
        }
        
    }
    
    
    
    
    return 0;
}