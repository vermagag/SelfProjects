#include<stdio.h>
#include<stdlib.h>
struct node{
	int data;
	struct node *link;
};

struct node *head;

void main()
{

	int op;
	printf("***MENU***");
	do
	{
	}
	switch(op)
	{	
		case 1:
			insert();
		case 2:
			delete();
		case 3:
			display();
		case4:
			exit(0);
		default:
		printf("Select right selection !!")

	}
	}while(op!=4);
	

}

void createlist()
{
	struct node =*ptr,*cur;
	int ele;
	head=NULL;
	ptr=head;
	printf("If you dont want to add element enter -1:\n");
	printf("please enter the elements which you want to allocate:\n");
	scanf("%d",&ele);
	while(ele!=-1)
	{
		cur = (struct node *) malloc(sizeof(struct node));
		cur->data = ele;
		cur->link = NULL;
		if(head==NULL)
		{
			head=cur;
		}
		else
		{
			ptr->link=cur;
			cur->link=head;
		}
	}
	

}
