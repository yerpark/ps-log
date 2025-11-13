#include <stdio.h>
#include <stdlib.h>

// 목표: 블록 링크드리스트로 큐 구현하기
    // 노드의 배열을 원형으로 구현하면 다른 노드가 있는 경우 순서가 깨짐
        // 노드의 순서를  .. 초기화도 하고 

typedef struct      s_node{
    int             arr[10000];
    int             headIdx;
    int             tailIdx;
    struct s_node   *next;
}                   t_node;

typedef struct      s_queue{
    t_node          *head;
    t_node          *tail;
}                   t_queue;

t_queue             *init_queue(void)
{
    t_queue     *myQueue;

    myQueue = (t_queue *)malloc(sizeof(t_queue));
    if (!myQueue)
        return (NULL);
    
    myQueue->head = (t_node *)malloc(sizeof(t_node));
    if(!myQueue->head)
    {
        free (myQueue);
        return (NULL);
    }
    myQueue->tail = myQueue->head;
    myQueue->head->headIdx = -1;
    myQueue->head->tailIdx = -1;
    myQueue->head->next = NULL;
}

t_queue 