import create_table
import insert
import argparse

def  main():
    parser=argparse.ArgumentParser(prog=None)
    subparser=parser.add_subparsers(title="uni_system")

    create_parser=subparser.add_parser("Create")
    create_parser.add_argument("-C" ,nargs=1)

    Read_parser=subparser.add_parser("Read")
    Read_parser.add_argument("-R",nargs=1)

    Update_parser=subparser.add_parser("Update")
    Update_parser.add_argument("-U",nargs=1)


    Delete_parser=subparser.add_parser("Delete")
    Delete_parser.add_argument("-D",nargs=1)


    args = parser.parse_args()
    print(args)

    # if args.command =="Create":
    if args.C:
        print("create")

    # if args.command =="Read":
    #     if args.R:
    #         print("Read")

    # if args.command =="Update":
    #     if args.U:
    #         print("Update")


    # if args.command =="Delete":
    #     if args.D:
    #         print("Delete")

# def  main():
#     create_table.create_table()
#     insert.insert_rows()

if __name__=="__main__":
    main()