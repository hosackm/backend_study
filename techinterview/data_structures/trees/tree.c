#include <stdio.h>
#include <stdlib.h>


// Tree type
typedef struct _tree_s* tree;
typedef struct _node_s* node;

struct _node_s
{
    int value;
    node left;
    node right;
} node_s;

struct _tree_s
{
    node root;
} tree_s;

// Tree public API
tree new_tree();
void destroy_tree(tree t);
int tree_insert(tree t, int value);
void print_tree(tree t);

// Tree private API
void _insert_value(node n, int value);
void _destroy_node(node n);
void _print_node(node n);

int main()
{
    tree t;

    t = new_tree();
    tree_insert(t, 6);
    tree_insert(t, 1);
    tree_insert(t, 2);
    tree_insert(t, 7);
    print_tree(t);
    destroy_tree(t);

    return 0;
}

tree new_tree()
{
    tree t;
    t = malloc(sizeof(tree_s));
    t->root = NULL;
    return t;
}

void destroy_tree(tree t)
{
    if(t->root)
    {
        _destroy_node(t->root);
    }
    free(t);
}

int tree_insert(tree t, int value)
{
    node n;
    if(t->root == NULL)
    {
        t->root = malloc(sizeof(node_s));
        t->root->left = NULL;
        t->root->right = NULL;
        t->root->value = value;
        return 0;
    }

    _insert_value(t->root, value);
    return 0;
}

void _insert_value(node n, int value)
{
    if(value < n->value)
    {
        if(n->left == NULL)
        {
            n->left = malloc(sizeof(node_s));
            n->left->value = value;
        }
        else
        {
            _insert_value(n->left, value);
        }
    }
    else
    {
        if(n->right == NULL)
        {
            n->right = malloc(sizeof(node_s));
            n->right->value = value;
        }
        else
        {
            _insert_value(n->right, value);
        }
    }
}

void _destroy_node(node n)
{
    if(n)
    {
        if(n->left)
        {
            _destroy_node(n->left);
        }
        if(n->right)
        {
            _destroy_node(n->right);
        }
        free(n);
    }
}

void print_tree(tree t)
{
    if(t && t->root)
    {
        _print_node(t->root);
    }
}

void _print_node(node n)
{
    if(n)
    {
        fprintf(stdout, "%d\n", n->value);
        _print_node(n->left);
        _print_node(n->right);
    }
}
