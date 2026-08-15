import numpy as np
import pandas as pd
import matplotlib.pyplot as p
import os as o

print('*'*70)
print('\t\t Welcome To Bakery Management System')
print('*'*70)

def add_item():
    df=pd.read_csv('Bakery.csv')
    p=df.iloc[-1,0]
    p=p+1
    k=input('--> Enter the Product Name (In Small Letters):')
    print('*'*70)
    if k in df.values:
        print('--> Same Product Exits')
        print('*'*70)
    else:
        m=int(input('--> Enter the Product price(in Rs):'))
        print('*'*70)
        l=float(input('--> Enter the Quantity(in Kg):'))
        df.loc[p-1]=[p,k,m,l]
        df.to_csv('Bakery.csv',index=False)
        print('*'*70)
        print('***Product Added Successfully***')
        print('*'*70)
        print(df.loc[p-1])
        print('*'*70)
    input()
    
def remove_item():
    nf=pd.read_csv('Bakery.csv')
    print('--> Press 1 To Remove with Product id')
    print('--> Press 2 To Remove with Product Name')
    print('*'*70)
    l=int(input('-->Enter Your Choice:'))
    if l==1:
        print('*'*70)
        i=int(input('--> Enter ProductId:'))
        if i-1 in nf.index:
            nf.drop(i-1,inplace=True)
            nf.to_csv('Bakery.csv',index=False)
            print('*'*70)
            print('***Product Remove Sucessfully***')
        else:
            print('No Product Found With This ProductId')
    elif l==2:
        print('*'*70)
        a=input('--> Enter the Product Name (In Small Letters):')
        if a in nf.values:
            df=nf[nf['productname']==a]
            x=df.index
            nf.drop(x,inplace=True)
            print('*'*70)
            print('***Product Remove Sucessfully***')
            nf.to_csv('Bakery.csv',index=False)
        else:
            print('***No Product Found With This name***')
    else:
        print('***Please Enter Valid Choice***')            
    input()

def update_item():
    df=pd.read_csv('Bakery.csv')
    productid=int(input('--> Enter The ProductId:'))
    print('*'*70)
    if productid -1 in df.index:
        x=int(input('--> Press 1 For Modify ProductName:')) 
        if x==1:
            print('*'*70)
            h=input('--> Enter New Name:')
            df.loc[productid -1,'productname']=h
            print('*'*70)
            print('***Name Updated Successfully***')
            print('*'*70)

        x=int(input('--> Press 2 For Modify ProductPrice(in Rs):'))     
        if x==2:
            print('*'*70)
            k=input('--> Enter New Price:')
            df.loc[productid -1,'productprice(in Rs)']=k
            print('*'*70)
            print('***Price Updated Successfully***')
            print('*'*70)
            
        x=int(input('--> Press 3 For Modify Quantity(in kg):'))        
        if x==3:
            print('*'*70)
            p=input('--> Enter Updated Quantity:')
            df.loc[productid -1,'quantity(in kg)']=p
            print('*'*70)
            print('***Quantity Updated Successfully***')
            print('*'*70)
        df.to_csv('Bakery.csv',index=False)
        
    else:
        print('*'*70)
        print('***Please Enter Valid Product Id***')
            
    input()

def search_item():
    nf=pd.read_csv('Bakery.csv')
    print('--> Press 1 To Search with Product id')
    print('--> Press 2 To Search with Product Name')
    print('*'*70)
    l=int(input('Enter Your Choice:'))
    if l==1:
        print('*'*70)
        code=int(input('--> Enter the Productid:'))
        if code -1 in nf.index:
            print('*'*70)
            print(nf.loc[code -1])
            print('*'*70)
        else:
            print('*'*70)
            print('***No Product Found With This Product Id***')
    elif l==2:
        print('*'*70)
        name=input('--> Enter the ProductName (In Small Letters):')
        if name in nf.values:
            print('*'*70)
            print(nf[nf['productname']==name])
        else:
            print('*'*70)
            print('***No Product Found With This Product Id***')
    else:
        print('***Please Enter Valid Choice***')        
    input()

def display_item():
    bf=pd.read_csv('Bakery.csv')
    print(bf)
    print('*'*70)
    input()

def Bar():
    df=pd.read_csv('Bakery.csv')
    print('*'*70)
    print('--> Press 1 - Product v/s Price')
    print('--> Press 2 - Product v/s Quantity')
    print('*'*70)
    s=int(input('--> Enter Your Choice:'))
    if s==1:
        p.bar(df['productname'],df['productprice(in Rs)'],color='indigo',lw=3,ls='solid',ec='cyan')
        p.xlabel('Product Name',fontsize=10)
        p.ylabel('product Price (In Rs)')
        p.title('Product v/s Price')
        p.savefig('bar1.jpg')
        p.show()
    elif s==2:
        p.bar(df['productname'],df['quantity(in kg)'],color='indigo',lw=3,ls='solid',ec='cyan')
        p.xlabel('Product Name',fontsize=10)
        p.ylabel('product Quantity (In Kg)')
        p.title('Product v/s Quantity')
        p.savefig('bar2.jpg')
        p.show()
    else:
        print('***Please Enter Valid Choice***')
    input()

def graphs():
    bf=pd.read_csv('Bakery.csv')
    print('--> Press 1 - Bar Chart')
    print('--> Press 2 - Histogram')
    print('*'*70)
    j=int(input('--> Enter your Choice:'))
    if j==1:
        Bar()
    elif j==2:
        p.hist(bf['productprice(in Rs)'],color='red',lw=2,ls='dashdot',ec='yellow')
        p.xlabel('Products Price',fontsize=10)
        p.ylabel('Product Quantity',fontsize=10)
        p.title('Number Of Product in Price Range',fontsize=12)
        p.savefig('Hist.jpg')
        p.show()
    else:
        print('*** Please Enter The Valid Choice***') 
    input()    
    
def Bakery():
    o.system('cls')
    while True:
        print('*'*70)
        print('\t\t Charlos Bakery Management menu')
        print('*'*70)
        print('--> Press 1 - Add Item')
        print('--> Press 2 - Remove Item')
        print('--> Press 3 - Update Item')
        print('--> Press 4 - Search Item')
        print('--> Press 5 - Display Items')
        print('--> Press 6 - Graphs')
        print('--> Press 7 - Exit')
        print('*'*70)
        ko=int(input('--> Enter Your Choice:'))
        print('*'*70)
        if ko==1:
            add_item()
        elif ko==2:
            remove_item()
        elif ko==3:
            update_item()
        elif ko==4:
            search_item()
        elif ko==5:
            display_item()
        elif ko==6:
            graphs()
        elif ko==7:
            print('***Thanks For Visiting***')
            print('   ***Data Updated***')
            print('*'*70)
            break
        else:
            print('*'*70)
            print('*** Please Enter Valid Choice***')
    input()

def search_order():
    pf=pd.read_csv('Customer.csv')
    code=int(input('--> Enter the billid:'))
    df=pf[pf['billid']==code]
    if df.empty:
        print('*'*70)
        print('***Order not exits***')
    else:
        print('*'*70)
        print(df)
    input()

def customer_bill():
    df=pd.read_csv('Bakery.csv')
    print('--> Available bakery product')
    print('*'*70)
    print(df)
    print('*'*70)
    code=int(input('-->Enter The product id of product to be Purchased :'))
    print('*'*70)
    if code -1 in df.index:
        qty=float(input('-->Enter the quantity to be purchased (in Kg) :'))
        if df.loc[code-1,'quantity(in kg)']<qty:
            print('*'*70)
            print('Product currently not')
        else:
            df.loc[code-1,'quantity(in kg)']-=qty
            df.to_csv('Bakery.csv',index=False)
            print('*'*70)
            amount=qty*df.loc[code-1,'productprice(in Rs)']
            print('-->Your Due Amount is:',amount)
            print('*'*70)
            name=input('-->Enter name of customer :')
            print('*'*70)
            bdate=input('-->Enter billing date in dd/mm/yyyy :')
            print('*'*70)
            df1=pd.read_csv('Customer.csv')
            if df1.empty:
                bill_id=1
                v=0
            else:
                bill_id=df1.iloc[-1,0]+1
                v=df1.index[-1]+1
            df1.loc[v]=[bill_id,name,bdate,amount,df.loc[code-1,'productname'],qty]
            df1.to_csv('customer.csv',index=False)
            print('***Bill generated sucessfully***')
            print('*'*70)
            print('***Thanks For Visiting Aur Bakery***')
            print('*'*70)
    else:
        print('No bakery product found with this productid')
    input()    
    

def show_all_cust_bill():
    bf=pd.read_csv('Customer.csv')
    print(bf)
    print('*'*70)               
    input()
    
def show_charts():
    kf=pd.read_csv('Customer.csv')
    kf1=kf.groupby('details')
    print('--> Press 1 - Bar Chart --> Most Selling Product')
    print('--> Press 2 - Line Chart --> Maximum Product sales vs Minimum Product sales')
    print('*'*70)
    k=int(input("--> Enter Your Choice:"))
    if k==1:
          s=kf1['orderamount'].sum()
          p.bar(s.index,s.values,color='indigo',ls='solid',ec='cyan')
          p.xlabel('Product name',fontsize=10)
          p.ylabel('Combined cost',fontsize=10)
          p.title('Most Selling Product',fontsize=10)
          p.savefig('sales.jpg')
          p.show()
    elif k==2:
          l=kf1['orderamount'].max()
          o=kf1['orderamount'].min()
          p.plot(l.index,l.values,color='orange',marker='o',lw=7,mfc='red',mec='yellow',ms=15,label='Maximum')
          p.plot(o.index,o.values,color='green',marker='o',lw=7,mfc='white',mec='black',ms=15,label='Minimum')
          p.xlabel('Product name',fontsize=10)
          p.ylabel('Price(in Rs)',fontsize=10)
          p.legend()
          p.title('Maximum Product sales vs Minimum Product sales',fontsize=10)
          p.savefig('max and min.jpg')
          p.show()
    else:
         print('***Please Enter Valid Choice***')
    input()

def Customer():
    o.system('cls')
    while True:
        print('*'*70)
        print('\t\t Charlos Bakery Customer Order menu')
        print('*'*70)
        print('--> Press 1 - Create Customer Order ') 
        print('--> Press 2 - Display Orders')
        print('--> Press 3 - Search Order')
        print('--> Press 4 - Show Chart Of Bills ')
        print('--> Press 5 - Quit')
        print('*'*70)
        k=int(input('-->Enter your choice:'))
        print('*'*70)
        if k==1:
            customer_bill()            
        elif k==2:
            show_all_cust_bill()
        elif k==3:
            search_order()
        elif k==4:
            show_charts()
        elif k==5:
            print('*** Quiting from Customer Order menu***')
            print('*'*70)
            break
        else:
            print('*'*70)
            print('***Please Enter Valid Choice***')
            print('*'*70)
    input()

while True:
    print('--> Press 1 - Bakery Management menu')
    print('--> Press 2 - Customer Billing Management menu')
    print('--> Press 3 - Quit')
    print('*'*70)
    m=int(input('-->Enter your choice :'))
    if m==1:
        Bakery()
        print('***Back To Main Menu***')
        print('*'*70)
    elif m==2:
        Customer()
        print('***Back To Main Menu***')
        print('*'*70)
    elif m==3:
        print('*'*70)
        print('***Thanks For Visiting***')
        break
    else:
        print('*'*70)
        print('***Please Enter Valid Choice***')
        print('*'*70)
    input()    


