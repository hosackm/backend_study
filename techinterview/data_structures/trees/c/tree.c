#include <stdlib.h>
#include <stdio.h>

// BST node data type
struct node
{
    int value;
    struct node* left;
    struct node* right;
};

// node functions
struct node* node_new(int value)
{
    struct node* n = malloc(sizeof(struct node));
    n->value = value;
    n->left = NULL;
    n->right = NULL;
    return n;
}

void node_destroy(struct node* n)
{
    if(n)
    {
        node_destroy(n->left);
        node_destroy(n->right);
        free(n);
    }
}

struct node* node_min_node_in_subtree(struct node* n)
{
    struct node* tmp = n;

    if(tmp)
    {
        while(tmp->left != NULL)
        {
            tmp = tmp->left;
        }
    }

    return tmp;
}

void node_insert(struct node* n, int value)
{
    if(value < n->value)
    {
        if(n->left == NULL)
        {
            n->left = node_new(value);
            return;
        }
        else
        {
            node_insert(n->left, value);
        }
    }
    else
    {
        if(n->right == NULL)
        {
            n->right = node_new(value);
            return;
        }
        else
        {
            node_insert(n->right, value);
        }
    }
}

struct node* node_delete(struct node* n, int value)
{
    if(n == NULL)
    {
        return NULL;
    }

    // search in left subtree
    if(value < n->value)
    {
        n->left = node_delete(n->left, value);
    }
    // search in righ subtree
    else if(value > n->value)
    {
        n->right = node_delete(n->right, value);
    }
    // found it
    else
    {
        struct node* tmp;

        // one child, promote right
        if(n->left == NULL)
        {
            tmp = n->right;
            free(n);
            return tmp;
        }
        // one child, promote left
        if(n->right == NULL)
        {
            tmp = n->left;
            free(n);
            return tmp;
        }

        // two children, copy minimum to this node and delete the original minimum
        // find minimum value in right subtree
        tmp = node_min_node_in_subtree(n->right);
        // replace this node with it's value
        n->value = tmp->value;
        // delete the original which is now a duplicate
        n->right = node_delete(n->right, tmp->value);
    }

    return n;
}

void node_print_inorder(struct node* n)
{
    if(n)
    {
        node_print_inorder(n->left);
        fprintf(stderr, "Node(%d)\n", n->value);
        node_print_inorder(n->right);
    }
}

// BST tree data type
struct tree
{
    struct node* root;
};

// BST tree functions
struct tree* new_tree()
{
    return malloc(sizeof(struct tree));
}

void tree_destroy(struct tree* t)
{
    node_destroy(t->root);
    free(t);
}

void tree_insert(struct tree* t, int value)
{
    if(t->root == NULL)
    {
        t->root = malloc(sizeof(struct node));
        t->root->left = NULL;
        t->root->right = NULL;
        t->root->value = value;
    }
    else
    {
        node_insert(t->root, value);
    }
}

void tree_delete(struct tree* t, int value)
{
    node_delete(t->root, value);
}

void tree_print_inorder(struct tree* t)
{
    fprintf(stderr, "Tree:\n");
    node_print_inorder(t->root);
}


int main(int argc, char* argv[])
{
    // create new tree
    struct tree *t = new_tree();

    // insert a bunch of nodes
    tree_insert(t, 50);
    tree_insert(t, 30);
    tree_insert(t, 20);
    tree_insert(t, 40);
    tree_insert(t, 70);
    tree_insert(t, 60);
    tree_insert(t, 80);

    // tree:
    //         50
    //     30      70
    //  20   40  60   80


    // 20->30->40->50->60->70->80
    tree_print_inorder(t);

    tree_delete(t, 20);
    // tree:
    //         50
    //     30      70
    //       40  60   80

    // 30->40->50->60->70->80
    tree_print_inorder(t);

    tree_delete(t, 30);
    // tree:
    //         50
    //     40      70
    //           60   80

    // 40->50->60->70->80
    tree_print_inorder(t);

    tree_delete(t, 50);
    // tree:
    //     60
    // 40      70
    //            80

    // 40->60->70->80
    tree_print_inorder(t);

    tree_destroy(t);

    return 0;
}
