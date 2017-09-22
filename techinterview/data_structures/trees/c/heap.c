#include <stdlib.h>
#include <stdio.h>

#define HEAP_BLOCK_SIZE 4096
#define LCHILD_OF(n) (2*n+1)
#define RCHILD_OF(n) (2*n+2)
#define PARENT_OF(n) ((n-1)/2)
#define HEAP_ERROR_NONE (0)
#define HEAP_ERROR_NULLPTR (-1)

// Heap Data Type
struct heap
{
    int *elements;
    size_t num_elements;
    size_t array_capacity;
};

// Public API
struct heap* heap_new();
void heap_destroy(struct heap* h);
void heap_insert(struct heap* h, int value);
int heap_pop(struct heap* h, int *value);
void heap_display(struct heap* h);

int main(int argc, char *argv[])
{
    int i;
    int ret;
    int out_val;
    int test_vals[] = {3, 1, 6, 5, 2, 4};
    struct heap *h = heap_new();

    // Fill the heap
    for(i = 0; i < sizeof(test_vals)/sizeof(int); ++i)
    {
        heap_insert(h, test_vals[i]);
    }

    // Display the heap. Should be: {1, 2, 4, 5, 3, 6}
    heap_display(h);

    // pop 1
    ret = heap_pop(h, &out_val);
    if(ret != HEAP_ERROR_NONE)
    {
        return ret;
    }

    // should be 2, 3, 4, 5, 6
    heap_display(h);

    heap_destroy(h);
    return 0;
}

// Private API
void _heapify_index_n_up(struct heap* h, int n);
void _heapify_index_n_down(struct heap* h, int n);

struct heap* heap_new()
{
    struct heap *h = malloc(sizeof(struct heap));
    h->elements = malloc(sizeof(int)*HEAP_BLOCK_SIZE);
    h->num_elements = 0;
    h->array_capacity = HEAP_BLOCK_SIZE;
    return h;
}

void heap_destroy(struct heap* h)
{
    if(h)
    {
        free(h->elements);
        free(h);
    }
}

void _heap_resize(struct heap* h)
{
    if(h)
    {
        h->array_capacity += HEAP_BLOCK_SIZE;
        h->elements = realloc(h->elements, sizeof(int)*h->array_capacity);
    }
}

void heap_insert(struct heap* h, int value)
{
    if(!h)
    {
        return;
    }

    if(h->num_elements == h->array_capacity)
    {
        _heap_resize(h);
    }

    // add new value to the end of the heap, satisfy heap property, and increment the number of elements in the heap
    h->elements[h->num_elements] = value;
    _heapify_index_n_up(h, h->num_elements);
    h->num_elements++;
}

int heap_pop(struct heap* h, int *value)
{
    if(!value || !h)
    {
        return HEAP_ERROR_NULLPTR;
    }

    // Copy top element into user supplied pointer
    *value = h->elements[0];
    // Move last element to the top of the heap
    h->elements[0] = h->elements[h->num_elements-1];
    // Indicate an element has been removed in num_elements;
    h->num_elements--;
    // Retain heap property
    _heapify_index_n_down(h, 0);

    return HEAP_ERROR_NONE;
}

void _heapify_index_n_up(struct heap* h, int n)
{
    int *parent;
    int *newvalue;

    // don't dereference null pointers
    if(!h)
    {
        return;
    }

    // reached the beginning of the heap
    if(n < 1)
    {
        return;
    }

    // check if the newvalue breaks the heap property
    parent = &h->elements[PARENT_OF(n)];
    newvalue = &h->elements[n];
    if(*newvalue < *parent)
    {
        // swap with parent to regain heap property
        int tmp = *newvalue;
        *newvalue = *parent;
        *parent = tmp;

        // recurse up through the parent to see if heap property satisfied
        _heapify_index_n_up(h, PARENT_OF(n));
    }

    return;
}

void _heapify_index_n_down(struct heap* h, int n)
{
    if(!h)
    {
        return;
    }

    // n is past the end of the heap
    if(n >= h->num_elements)
    {
        return;
    }

    // If there is a right child and it's smaller than the left. Check to swap with parent
    if(RCHILD_OF(n) < h->num_elements && h->elements[RCHILD_OF(n)] < h->elements[LCHILD_OF(n)])
    {
        int *thisvalue = &h->elements[n];
        int *rchild = &h->elements[RCHILD_OF(n)];

        if(*thisvalue > *rchild)
        {
            int tmp = *thisvalue;
            *thisvalue = *rchild;
            *rchild = tmp;
            _heapify_index_n_down(h, RCHILD_OF(n));
        }
    }
    // If there is a left child swap it with the parent
    else if(LCHILD_OF(n) < h->num_elements)
    {
        int *thisvalue = &h->elements[n];
        int *lchild = &h->elements[LCHILD_OF(n)];

        if(*thisvalue > *lchild)
        {
            int tmp = *thisvalue;
            *thisvalue = *lchild;
            *lchild = tmp;
            _heapify_index_n_down(h, LCHILD_OF(n));
        }
    }

    return;
}

void heap_display(struct heap* h)
{
    int i;

    if(!h)
    {
        return;
    }

    for(i = 0; i < h->num_elements; ++i)
    {
        if(i > 0)
        {
            fprintf(stdout, ", ");
        }
        fprintf(stdout, "%d", h->elements[i]);
    }
    fprintf(stdout, "\n");
}
