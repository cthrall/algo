import java.util.ArrayList;

public class LinkedList
{
    public class Node
    {
	private Object value;
	private Node node;

	public Node(Object value)
	{
	    this.value = value;
	}

	public String toString()
	{
	    return "Value: " + value;
	}

	public Node getNext() { return node; }
	public void setNext(Node n) { node = n; }
	
	public Object getValue() { return value; }
    }

    private Node root;

    public int length()
    {
	return _length(root, 1);
    }

    private int _length(Node node, int d)
    {
	if (node.getNext() != null)
	    return _length(node.getNext(), d + 1);

	return d;
    }

    public ArrayList walk()
    {
	ArrayList output = new ArrayList();

	return _walk(output, root);
    }

    public ArrayList _walk(ArrayList output, Node node)
    {
	output.add(node.getValue());

	if (node.getNext() != null)
	    _walk(output, node.getNext());

	return output;
    }

    public void insert(Object value)
    {
	if (root == null)
	    root = new Node(value);
	else
	    _insert(root, value);
    }

    public void _insert(Node node, Object value)
    {
	if (node.getNext() == null)
	{
	    node.setNext(new Node(value));
	}
	else
	{
	    _insert(node.getNext(), value);
	}
    }

    public static void main(String[] args)
    {
	LinkedList list = new LinkedList();
	int[] inputs = new int[] {
	    1, 2, 3, 4, 5 };

	for (int i = 0; i < inputs.length; i++)
	{
	    list.insert(inputs[i]);
	}

	System.out.println(list.length());
	ArrayList output = list.walk();
	StringBuilder sb = new StringBuilder();
	for (int i = 0; i < output.size(); i++)
	{
	    sb.append(output.get(i)).append(" ");	    
	}

	System.out.println(sb.toString());
    }
}
