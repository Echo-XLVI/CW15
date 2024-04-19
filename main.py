from connection import Connection
import crud
import create_table
import insert

import argparse

def  main():
    conn = Connection.connect('localhost','postgres',5648,'1380ACreZA46','universitydb')

    parser=argparse.ArgumentParser(prog=None)
    subparser=parser.add_subparsers(title="uni_system",dest='command')

    create_parser=subparser.add_parser("Create")
    create_parser.add_argument("-C" ,nargs="*")
    create_parser.set_defaults(func=crud.insert)
    Read_parser=subparser.add_parser("Read")
    Read_parser.add_argument("-R",nargs=1)
    Read_parser.set_defaults(func=crud.show)

    Update_parser=subparser.add_parser("Update")
    Update_parser.add_argument("-U",nargs=4,help="args=table_name,column,new_value,id")
    Update_parser.set_defaults(func=crud.update)


    Delete_parser=subparser.add_parser("Delete")
    Delete_parser.add_argument("-D",nargs=2)
    Delete_parser.set_defaults(func=crud.delete)


    args = parser.parse_args()

    if args.command=='Create':        
        args.func(conn,*args.C)
    if args.command=='Read':    
        args.func(conn,*args.R)
    elif args.command=='Update':
        args.func(conn,*args.U)        
    elif args.command=='Delete':
        args.func(conn,*args.D)                

# def  main():
#     create_table.create_table()
#     insert.insert_rows()

if __name__=="__main__":
    main()