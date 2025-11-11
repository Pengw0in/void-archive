class returnvalue
{
    String name="cyber";
    public String getname()
    {
        System.out.println("name is: " + name);
        return name;
    }
    public static void main(String args[])
    {
        returnvalue re = new returnvalue();
        String result = re.getname();
        System.out.println("Returned value: " + result);
    }
}