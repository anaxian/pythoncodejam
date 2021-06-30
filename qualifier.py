from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """

    max_length_of_column= []
    no_of_rows= len(rows)
    no_of_columns=len(rows[0])
    col=[]
    has_labels=True
    if labels==[]:
        has_labels=False
    print(has_labels)

    def transpose(l1, l2):
 
        # iterate over list l1 to the length of an item
        for i in range(len(l1[0])):
            # print(i)
            row =[]
            for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
                row.append(item[i])
            l2.append(row)
        return l2
    columns=transpose(rows,[])
   

    for eachitemcolumn in columns:
        columnitem=[]
        for one in eachitemcolumn:
            columnitem.append(str(one).lower())
        max_length_of_column.append(len(max(columnitem,key=len)))
  
    length=sum(max_length_of_column)
    
   

  
    x="  ┌"+"─"*(length+2*no_of_columns)+"──┐\n "
    for each in labels:
        if centered:
            titlecenterpadding= max_length_of_column[int(labels.index(each))]-len(str(each))
            x=x+" | "
            x=x+(" "*int((titlecenterpadding)//2))
            x=x+str(each)
            x=x+(" "*int(((titlecenterpadding)//2)+titlecenterpadding%2))
           
        else:
            x = x+" | "+str(each)
            x= x+(" "*(max_length_of_column[int(labels.index(each))]-len(str(each))))
    x=x+" |\n"

    #toprow
    #toprow
    print(max_length_of_column)
    max_length_of_column_tuple=tuple(max_length_of_column)
    if has_labels:
        x = x+"  ├"
    else:
        x = x+"  ┌"
    x = x+"─"*(length+2*no_of_columns)+"──"
    if has_labels:
        x=x+ "┤\n "
    else: 
        x=x+ "┐\n "
    for eachrow in rows:
        for item in eachrow:
            if centered:
                centre_pad= (max_length_of_column_tuple[int(eachrow.index(item))]-len(str(item)))//2
                x = x+" | "
                x = x+(" "*centre_pad) 
                x=x+str(item)
                if (len(str(item))-max_length_of_column_tuple[int(eachrow.index(item))])%2!=0:
                    x=x+" " 
                x = x+(" "*(centre_pad))
                
                
            else: 
                x = x+" | "+str(item)
                x= x+(" "*(max_length_of_column_tuple[int(eachrow.index(item))]-len(str(item))))
        x=x+" |\n "
    x=x+" └"+"─"*(length+2*no_of_columns)+"──┘"


    return x
    

table = make_table(
    rows=[
        ["Lemon", 18_3285, "Owner"],
        ["Sebastiaan", 18_3285.1, "Owner"],
        ["KutieKatj", 15_000, "Admin"],
        ["Jake", "MoreThanU", "Helper"],
        ["Joe", -12, "Idk Tbh"]
    ],
    labels=["User", "Messages", "Role"], centered=True,
)
print(table)