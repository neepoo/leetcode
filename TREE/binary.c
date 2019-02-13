#include <stdlib.h>
#include <stdio.h>

typedef struct node
{
    /* data */
    int data;
    struct node *left;
    struct node *right;
} Node;

void pre_order(Node *node)
{
    // 根 --> 左 --> 右
    if (node != NULL)
    {
        printf("%d\n", node->data);
        pre_order(node->left);
        pre_order(node->right);
    }
}

int main()
{
    Node n1;
    Node n2;
    Node n3;
    Node n4;

    n1.data = 56666;
    n2.data = 6;
    n3.data = 7;
    n4.data = 8;

    n1.left = &n2;
    n1.right = &n3;
    n2.left = &n4;
    n2.right = NULL;
    n3.left = NULL;
    n3.right = NULL;
    n4.left = NULL;
    n4.right = NULL;

    pre_order(&n1);
}