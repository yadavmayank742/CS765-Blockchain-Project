from Blockchain import Blockchain

def show_menu(selected_blockchain_name):
    while True:
        if selected_blockchain_name == "":
            options_string = f"""
        Choose the operation:
                1. Create New Blockchain.
                2. List existing Blockchains.
                3. Select Blockchain.
                4. Show selected blockchain content.
                5. Add new block to the selected blockchain.
                6. Delete Selected Blockchain.
                7. Exit (it will destroy all the blockchains!)

        Enter your choice (1-7): """

        else:
            options_string = f"""
        Choose the operation: [ Currently selected Blockchain is `{selected_blockchain_name}`]
                1. Create New Blockchain.
                2. List existing Blockchains.
                3. Select Blockchain.
                4. Show selected blockchain content.
                5. Add new block to the selected blockchain.
                6. Delete Selected Blockchain - `{selected_blockchain_name}`.
                7. Exit (it will destroy all the blockchains!)

        Enter your choice (1-7): """

        choice = input(f"{options_string}").strip()

        if not choice:
            print("No input provided. Please enter a number between 1 and 7.")
            continue

        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        choice = int(choice)
        if 1 <= choice <= 7:
            return choice
        else:
            print("Choice out of range. Please enter a number between 1 and 7.")

def list_blockchains(all_blockchains):
    if(len(all_blockchains) != 0):
        print(f"\nThe Existing Blockchains are: ")
        for index, (name, _) in enumerate(all_blockchains.items()):
            print(f"\t{index+1}. {name}")
    else:
        print(f"NO blockchains created!")



def choose_blockchain(blockchain_dict):
    existing_blockchains_list = ""
    temp_dict = {}  # number: original_name

    for index, (name, _) in enumerate(blockchain_dict.items()):
        temp_dict[index] = name  # keep original case here
        existing_blockchains_list += f"{index + 1}. {name}\n"

    while True:
        choice = input(f"""{existing_blockchains_list}
Choose the blockchain to work with: """).strip()

        if not choice:
            print(f"No input provided. Please enter a number between 1 and {len(blockchain_dict)}.")
            continue

        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        choice = int(choice)

        if not (1 <= choice <= len(blockchain_dict)):
            print(f"Wrong entry, please enter a number between 1 and {len(blockchain_dict)}.")
            return choose_blockchain(blockchain_dict)

        selected_name = temp_dict[choice - 1]
        print(f"Selected {selected_name}")
        return selected_name




def main():
    all_blockchains = {} # name, blockchain
    choice = 0;
    selected_blockchain_name = None

    while choice != 7:
        choice = show_menu(selected_blockchain_name);

        match choice:
            case 1: # create new blockchain
                new_blockchain_name = input(f"\nEnter Name for the new Blockchain: ")
                if(new_blockchain_name): new_blockchain = Blockchain(name = new_blockchain_name.lower());
                else: new_blockchain = Blockchain(name = f"Blockchain Number {len(all_blockchains)+1}".lower());
                all_blockchains[new_blockchain_name] = new_blockchain;
                print(f"Successfully Created New Blockchain named `{new_blockchain_name.lower()}`")

            case 2: # list existing blockchains
                list_blockchains(all_blockchains);
            case 3: # select blockchain
                if(len(all_blockchains) != 0):
                    selected_blockchain_name = choose_blockchain(all_blockchains);
                    print(f"Selected Blockchain `{selected_blockchain_name}`. ")
                else:
                    print(f"No blockchains crated so far, create one to start with!.")

            case 4: # show selected blockchain
                if(selected_blockchain_name):
                    selected_blockchain = all_blockchains[selected_blockchain_name]
                    selected_blockchain.show_blockchain();
                else:
                    print(f"No blockchain selected, select first!")

            case 5: # add new block to selected blockchain
                if(selected_blockchain_name):
                    selected_blockchain = all_blockchains[selected_blockchain_name];
                    selected_blockchain.add_block()
                else:
                    print(f"No blockchain selected!")

            case 6: # delete selected blockchain
                if(selected_blockchain_name):
                    selected_blockchain = all_blockchains[selected_blockchain_name];
                    prompt = input(f"""
                                   Are you sure you want to delete {selected_blockchain_name},
                                   it has {len(selected_blockchain.chain)} Blocks in it?
                                   Yes/No? : """)
                    if 'y' in prompt.lower():
                        del all_blockchains[selected_blockchain_name]
                        print(f"Deleted Blockchain `{selected_blockchain_name}` permanently!")
                    else:
                        print(f"Not Deleting Blockchain `{selected_blockchain_name}`.")
                else:
                    print(f"No blockchain selected!")

            case 7:
                print(f"All the blockchains destroyed!")
                break;

            case _: # in case thw input in not in range 1 to 7
                print(f"Invalid Choice, please reselect.");

    return 0;


if __name__ == "__main__":
    main()