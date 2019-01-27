#include<stdio.h>
#include<stdlib.h>
/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
//  struct ListNode {
//       int val;
//       struct ListNode *next;
//  }*List;
struct ListNode {
     int val;
      struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *res,*pt,*node; // 创建三个结构指针
    int j = 0, temp = 0;  // j代表是否产生了进位， temp则是两个链表统一位置val之和。j=0因为一开始不可能就产生了进位
    res = (struct ListNode*)malloc(sizeof(struct ListNode));  // 开辟一块空间指向节点
    res->next=NULL;  // res是链表的最后一个元素，此时val并为分配value
    pt=res; // pt指向res所指向的区域
    while(l1 != NULL || l2 != NULL || j!= 0){  // 之前没有考虑到假如两链表长度不一样的情况，也没有考虑到产生了进位应该新创建一个node
        node = (struct ListNode*)malloc(sizeof(struct ListNode));  // 创建node
        temp = (l1 ? l1->val : 0) + (l2 ? l2-> val : 0) + j; // 注意有一个+j
        node->val = temp%10; // 妙
        j = temp/10;
        node->next = NULL;
        pt->next=node;
        pt = node;// 点睛之笔
        l1 = l1 ? l1->next :l1;
        l2 = l2 ? l2->next: l2;
    }
    pt =res->next;
    free(res);
    return pt;

}

