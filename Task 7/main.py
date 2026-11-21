
import re
import time

contacts = [
    {
        "name": "Dr. Ravi",
        "phone": "+91 98400 12345",
        "email": "ravi@gmail.com"
    },
    {
        "name": "Ravi Kumar",
        "phone": "9840012345",
        "email": "ravi.kumar@gmail.com"
    },
    {
        "name": "Arun",
        "phone": "9876543210",
        "email": "arun@gmail.com"
    },
    {
        "name": "Dr. Ravi",
        "phone": "9840012345",
        "email": "ravi@gmail.com"
    },
    {
        "name": "Priya",
        "phone": "",
        "email": "priya@gmail.com"
    }
]

# Normalize phone number
def normalize_phone(phone):
    digits = re.sub(r"\D", "", phone)

    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]

    return digits

# Normalize name
def normalize_name(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())

# Contact merging
def merge_contacts(contacts):
    groups = []
    phone_index = {}
    email_index = {}

    for contact in contacts:
        name = contact.get("name", "").strip()
        phone = contact.get("phone", "").strip()
        email = contact.get("email", "").strip().lower()

        normalized_phone = normalize_phone(phone)
        normalized_name = normalize_name(name)

        # Find existing matching contacts
        matches = set()

        if normalized_phone and normalized_phone in phone_index:
            matches.add(phone_index[normalized_phone])

        if email and email in email_index:
            matches.add(email_index[email])

        if matches:
            main = min(matches)

            groups[main]["names"].add(name)
            groups[main]["normalized_names"].add(normalized_name)

            if phone:
                groups[main]["phones"].add(phone)

            if normalized_phone:
                groups[main]["normalized_phones"].add(normalized_phone)

            if email:
                groups[main]["emails"].add(email)

            # Merge other matching groups
            for old in sorted(matches - {main}):
                if groups[old] is not None:
                    for key in groups[main]:
                        groups[main][key].update(groups[old][key])

                    groups[old] = None

        else:
            main = len(groups)

            groups.append({
                "names": {name} if name else set(),
                "normalized_names": {normalized_name} if normalized_name else set(),
                "phones": {phone} if phone else set(),
                "normalized_phones": {normalized_phone} if normalized_phone else set(),
                "emails": {email} if email else set()
            })

        # Update indexes
        for number in groups[main]["normalized_phones"]:
            phone_index[number] = main

        for mail in groups[main]["emails"]:
            email_index[mail] = main

        # Update indexes after merging
        for i, group in enumerate(groups):
            if group is not None:
                for number in group["normalized_phones"]:
                    phone_index[number] = i

                for mail in group["emails"]:
                    email_index[mail] = i

    return [group for group in groups if group is not None]


# Display merged contacts
result = merge_contacts(contacts)

for i, contact in enumerate(result, start=1):
    print("\nContact", i)
    print("Names:", contact["names"])
    print("Phone numbers:", contact["phones"])
    print("Emails:", contact["emails"])

print("\nTotal merged contacts:", len(result))

# Measure execution time
for size in [1000, 100000]:
    test_contacts = [
        {
            "name": "Person " + str(i),
            "phone": str(9000000000 + i),
            "email": "person" + str(i) + "@gmail.com"
        }
        for i in range(size)
    ]

    start = time.time()
    merge_contacts(test_contacts)
    end = time.time()

    print(size, "contacts time:", end - start, "seconds")
