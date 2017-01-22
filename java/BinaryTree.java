import java.util.ArrayList;

public class BinaryTree
{
    public class Node
    {
	private int value;
	private Node left;
	private Node right;
	
	public Node(int value)
	{
	    this.value = value;
	}

	public String toString()
	{
	    return "Value: " + value;
	}
	
	public Node getLeft() { return left; }
	public void setLeft(Node n) { left = n; }

	public Node getRight() { return right; }
	public void setRight(Node n) { right = n; }

	public int getValue() { return value; }
    }

    private Node root;

    public int depth()
    {
	return _depth(root, 1);
    }

    private int _depth(Node node, int d)
    {
	if (node.getLeft() != null)
	    return _depth(node.getLeft(), d + 1);
	    
	if (node.getRight() != null)
	    return _depth(node.getRight(), d + 1);

	return d;
    }

    public ArrayList[] walk()
    {
	int depth = depth();
	ArrayList[] output = new ArrayList[depth];

	return _walk(output, root, 0);
    }

    public ArrayList[] _walk(ArrayList[] output, Node node,
			 int level)
    {
	if (output[level] == null)
	    output[level] = new ArrayList();
	
	output[level].add(node.getValue());

	if (node.getLeft() != null)
	    _walk(output, node.getLeft(), level + 1);

	if (node.getRight() != null)
	    _walk(output, node.getRight(), level + 1);

	return output;
    }
    
    public void insert(int value)
    {
	if (root == null)
	    root = new Node(value);
	else
	    _insert(root, value);
    }

    public void _insert(Node node, int value)
    {
	if (node.getValue() == value)
	    return;
	else
	{
	    if (value < node.getValue())
	    {
		if (node.getLeft() == null)
		    node.setLeft(new Node(value));
		else
		    _insert(node.getLeft(), value);
	    }
	    else
	    {
		if (node.getRight() == null)
		    node.setRight(new Node(value));
		else
		    _insert(node.getRight(), value);
	    }
	}
    }
    
    public static void main(String[] args)
    {
	BinaryTree tree = new BinaryTree();
	int[] inputs = new int[] {
	    11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31 };

	for (int i = 0; i < inputs.length; i++)
	{
	    tree.insert(inputs[i]);
	}

	System.out.println(tree.depth());
	ArrayList[] output = tree.walk();
	for (int i = 0; i < output.length; i++)
	{
	    String level = "";
	    for (int j = 0; j < output[i].size(); j++)
	    {
		level += output[i].get(j) + " ";
	    }
	    
	    System.out.println("Level " + i + ": " + level);
	}
    }
}
