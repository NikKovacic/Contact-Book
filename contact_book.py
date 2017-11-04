#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Contact:
    def __init__(self, first_name, last_name, birth_year, address, phone_number,  email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def get_full_name(self):
        return self.first_name + " " + self.last_name


def list_all_contact(contacts):
    for index, person in enumerate(contacts):
        print "ID: " + str(index)
        print person.get_full_name()
        print person.birth_year
        print person.address
        print person.phone_number
        print person.email
        print ""  # empty line

    if not contacts:
        print "The contact list is empty"


def add_new_contact(contacts):
    first_name = raw_input("Please enter contact's first name: ")
    last_name = raw_input("Please enter contact's last name: ")
    birth_year = raw_input("Please enter contact's birth year: ")
    address = raw_input("Please enter contact's address: ")
    phone = raw_input("Please enter contact's phone number: ")
    email = raw_input("Please enter contact's email: ")

    new = Contact(first_name=first_name, last_name=last_name, birth_year=birth_year, address=address,
                  phone_number=phone, email=email)
    contacts.append(new)

    print ""  # empty line
    print new.get_full_name() + "was successfully added to contact list."


def edit_contact(contacts):
    print "Select the number of the contact you'd like to edit: "

    for index, person in enumerate(contacts):
        print str(index) + ") " + person.get_full_name()

    print ""  # empty line
    selected_id = raw_input("What contact would you like to edit? (enter ID number): ")
    selected_contact = contacts[int(selected_id)]

    new_first_name = raw_input("Please enter a new first name for %s: " % selected_contact.get_full_name())
    selected_contact.first_name = new_first_name

    print ""  # empty line
    print "First name updated."

    new_last_name = raw_input("Please enter a new last name for %s: " % selected_contact.get_full_name())
    selected_contact.last_name = new_last_name

    print ""  # empty line
    print "Last name updated."

    new_birth_year = raw_input("Please enter a new birth year for %s: " % selected_contact.get_full_name())
    selected_contact.birth_year = new_birth_year

    print ""  # empty line
    print "Birth year updated."

    new_address = raw_input("Please enter a new address for %s: " % selected_contact.get_full_name())
    selected_contact.address = new_address

    print ""  # empty line
    print "Address updated."

    new_phone_number = raw_input("Please enter a new phone number for %s: " % selected_contact.get_full_name())
    selected_contact.phone_number = new_phone_number

    print ""  # empty line
    print "Phone number updated."

    new_email = raw_input("Please enter a new email for %s: " % selected_contact.get_full_name())
    selected_contact.email = new_email

    print ""  # empty line
    print "Email updated."


def delete_contact(contacts):
    print "Select the number of contact you'd like to delete: "

    for index, person in enumerate(contacts):
        print str(index) + ") " + person.get_full_name()

        print ""  # empty line
        selected_id = raw_input("What contact would you like to delete? (enter ID number): ")
        selected_contact = contacts[int(selected_id)]

        contacts.remove(selected_contact)
        print ""  # empty line
        print "Contact was successfully removed from your contact list."


def main():
    print "Welcome to your Contact List."

    maks = Contact(first_name="Maks", last_name="Klanar", birth_year="1996", address="Pustal 7",
                   phone_number="041222444", email="max.klanar@gmail.com")
    nika = Contact(first_name="Nika", last_name="Maglic", birth_year="1999", address="Koroška cesta 12",
                   phone_number="080999421", email="nika.maglic99@gmail.com")
    ajda = Contact(first_name="Ajda", last_name="Punaver", birth_year="1993", address="Domzalska ulica 44",
                   phone_number="040666110", email="ajda.punaver@hotmail.com")
    kim = Contact(first_name="Kim", last_name="Davba", birth_year="1997", address="Vincarje 3",
                  phone_number="030717383", email="davba_kim@gmail.com")
    primoz = Contact(first_name="Primoz", last_name="Sterben", birth_year="1982", address="Koprska cesta 204",
                     phone_number="071999777", email="primoz.sterben@siol.si")
    contacts = [maks, nika, ajda, kim, primoz]

    while True:
        print ""  # empty line
        print "Plese choose one of these options: "
        print "a) See all your contacts"
        print "b) Add a new contact"
        print "c) Edit a contact"
        print "d) Delete a contact"
        print "e) Quit the program."
        print ""  # empty line

        selection = raw_input("Please enter your selection (a, b, c, d or e): ")
        print ""  # empty line

        if selection.lower() == "a":
            list_all_contact(contacts)
        elif selection.lower() == "b":
            add_new_contact(contacts)
        elif selection.lower() == "c":
            edit_contact(contacts)
        elif selection.lower() == "d":
            delete_contact(contacts)
        elif selection.lower() == "e":
            print "Thank you for using Contact List. Goodbye!"
            break
        else:
            print "Sorry, I didn't understand your selection. Please try again."
            continue


if __name__ == '__main__':
    main()
