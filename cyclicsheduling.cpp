#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<math.h>
using namespace std ;

struct Node
{
   int i , j , deadline, exe_time ;
   struct Node * next ;

  } ;

typedef struct Node NODE ;

NODE* Create_Node(int i , int j, int deadline, int exe_time)
 {
NODE*N = (NODE*)malloc(sizeof(NODE)) ;
N->i = i ;
N->j = j ;
N->deadline= deadline ;
N->exe_time = exe_time ;
N->next = NULL ;
return N ;
}

NODE *front = NULL, *rear = NULL ;

void InsertNode(int k , int j , int deadline, int exe_time)
{
   NODE *Task ;
   
 Task = Create_Node(k ,  j,  deadline,  exe_time) ;
  
  if(front == rear && front == NULL)
   {
 
    front = rear = Task ;
    front->next = NULL ;
    rear->next = NULL ;

   }

   else
{

  rear->next = Task ;
  rear = Task ;
  rear->next = NULL ;

  }



 }

void Display() 
{

  NODE *tmp = front ;
  while(tmp != NULL)
   {
     cout << "\n" << tmp->i << "," << tmp->j << "->" ;
	tmp = tmp->next ;
   }
 }

void sortEDF()
 {
  for(NODE *M = front; M != rear; M= M->next)
{

  for(NODE *N = front; N != rear; N= N->next)
   {

     NODE *tmp = N->next ;
     int info ;
     if(N->deadline > tmp->deadline)
      {
         info = N->i ;
         N->i = tmp->i ;
         tmp->i = info ;
 
         info = N->j ;
         N->j = tmp->j;
 	 tmp->j = info ;
 
	info = N->deadline ;
 	N->deadline = tmp->deadline ;
 	tmp->deadline = info ;

 	info = N->exe_time ;
 	N->exe_time = tmp->exe_time ;
 	tmp->exe_time = info ;

 

      }



  }
 }

}


void Schedule(int k, int size)
 {

    int t = size ;
  	NODE *t1 = front ;
     for(NODE *M = front ; M != NULL; M=M->next)
   {
 
       if(M->exe_time <= t)
  {
        t-= M->exe_time ;
        cout << "\nExecuted Task:(" << M->i << " " << M->j << ")";
        cout << "\nCurrent Time: " << k+size-t << "\n" ;

 	if(front == rear)
         {
 
            front = NULL ;
 	    rear = NULL ;
    }
        else if(M == front)
          {
            NODE *tmp = M ;
 	    front = front->next ;
	   free(tmp) ;
          }
          else
        {
          NODE *tmp = M ;
          t1->next = M->next ;
          free(tmp) ;
       }

   }
      t1 = M ;
  }
}

int gcd(int m , int n)
 {

   if(m == 0)
     return n ;
   else
     gcd(n%m, m) ;


 }


int maximum(int T[20], int size)
{

   
 int max = T[0] ;
 
 for(int i = 1 ; i < size ; i++)
 {
     if(T[i] > max)
      max = T[i] ;
     
    
  }

return max ;


}



int minimum(int T[20], int size)
{

 int min = T[0] ;
 
 for(int i = 1 ; i < size ; i++)
 {
     if(T[i] < min)
      min = T[i] ;
     
    
 }

return min ;




}
int HyperPeriod(int T[20], int size)
{
 
 

 // Calculating the LCM of Periods

int a = 1 ;
int  b = maximum(T, size);

//cout << b << "\n" ;

 while(a != 0)
 {
 
  a = 0 ;
 for(int i = 0 ; i < size ; i++)
 {
 	//cout << T[i] << "\n" ;
     if((b%T[i]) != 0)
      {  a = 1 ;
     }
       

  
 }
// cout << "a" << a << "\n" ;
 b++ ;
 }

return b-1 ;

  }



int main()
{

 int R[20], C[20], T[20] , D[20] , n ;
 
 cout << "Enter the number of Tasks" ;
 cin >> n ;
 
 cout << "Enter the Tasks" ;
 
 
 for(int i = 0 ; i < n ; i++)
 {
 
  cout << "Enter the Phase, Completion, TimePeriod and Deadline for process" << i+1 ;
  cin >> R[i] >> C[i] >> T[i] >> D[i] ;
 
 }
 
 
 
 // Calculating the HyperPeriod 
 int hyperPeriod = HyperPeriod(T, n) ;


// Checking conditions for frame

 //writing factors of HyperPeriod

int frame_f[100], j = -1  ;
 for(int i = 1 ; i < hyperPeriod ; i++)
 {
  if(hyperPeriod%i == 0)
   frame_f[++j] = i ;
 }

int frame_size[20] ;
int k = 0 ;
for(int i= 0 ; i < j ; i++)
   {
    if((frame_f[i] >= maximum(C, n)) && (frame_f[i] <= minimum(D, n)))
      frame_size[k++] = frame_f[i] ;


   }

   

   // Cheking Integral No.

int frame_s = -1;
for(int j = 0 ; j < k ; j++)
{
 for(int i = 0 ; i < n ; i++)
  {
    if((floor(T[i]/frame_size[j]) - T[i]/frame_size[j] == 0) && ((2*frame_size[j] - gcd(T[i], frame_size[j]) )  <=D[i]))   
      {  
      	  frame_s = frame_size[j] ;

//        return 0 ;
      }

  }  


  }


// frame is
  
 
  if(frame_s == -1)
  { 
  	 cout << "Cannot be schedulable" ;

  }else
  {
  cout << "\nFrame is " << frame_s << "\n";
   }

float sumutil = 0 , util ;
for(int i = 0 ; i < n ; i++)
 {
    
     util = (float)C[i]/(float)T[i] ;
     sumutil += util ;
     

    


  }

cout << "\nUtilization factor: " << sumutil  << "\n\n";



  int Schd[hyperPeriod] , temp = 0;

// Tasks instances   // Tasks Instances Deadline
  int Tasks[n][hyperPeriod] , Deadline[n][hyperPeriod] ;

  for(int i = 0 ; i < n ; i++)
  {
       temp = 0 ;
       for(j = 0 ; j < hyperPeriod/T[i] ; j++)
       {
        Tasks[i][j] = temp ;
        temp += T[i] ; 
        cout <<  Tasks[i][j] << " " ;
               }
               cout << "\n" ;
  }



  // Deadline of Instances
  for(int i = 0 ; i < n ; i++)
  {  temp = 0 ;
       for(j = 0 ; j < hyperPeriod/T[i] ; j++)
       {
          temp += D[i] ;
        Deadline[i][j] = temp ; 
        cout <<  Deadline[i][j] << " " ;
               }


   
    cout << "\n" ;


  }







  for(int i  = 0 ; i < hyperPeriod ; i+=frame_s)
 
  {
       for(int k =0 ; k < n ; k++)
         {
                for(int j = 0 ; j < hyperPeriod/T[k]; j++)
                   {
                      if(Tasks[k][j] != -1 && Tasks[k][j] <= i)
                      {  InsertNode(k, j ,Deadline[k][j], C[k]) ;
                        Tasks[k][j] = -1 ;
                
                      }
                     }
 
  }     

  Display() ;
  
  sortEDF() ;
  
 cout << "\nSorted: \n" ;
 Display() ;
 Schedule(i, frame_s) ;
 cout << "\n" ;
 Display() ;
 cout << "\n" ;
     
  }




return 0 ;
}


