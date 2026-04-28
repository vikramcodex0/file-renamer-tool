import os
import argparse

def rename_files(folder_path, prefix, start_num=1, file_type=""):

    if not os.path.exists(folder_path):
        print("❌ Folder not found")
        return

    files = sorted(os.listdir(folder_path))
    count = start_num

    for file in files:
        old_path = os.path.join(folder_path, file)

        if os.path.isfile(old_path):

            # skip already renamed
            if file.startswith(prefix + "_"):
                continue

            # filter file type
            if file_type and not file.endswith(file_type):
                continue

            # remove spaces
            clean_file = file.replace(" ", "_")

            extension = os.path.splitext(clean_file)[1]

            new_name = f"{prefix}_{count}{extension}"
            new_path = os.path.join(folder_path, new_name)

            # avoid overwrite
            if os.path.exists(new_path):
                print(f"⚠ Skipping {new_name}")
                continue

            os.rename(old_path, new_path)
            print(f"✅ {file} → {new_name}")

            count += 1

    print("\n🎉 Renaming completed!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Renamer Tool")

    parser.add_argument("--folder", required=True, help="Folder path")
    parser.add_argument("--prefix", required=True, help="New file prefix")
    parser.add_argument("--start", type=int, default=1, help="Starting number")
    parser.add_argument("--ext", default="", help="File extension (.jpg etc)")

    args = parser.parse_args()

    rename_files(
        folder_path=args.folder,
        prefix=args.prefix,
        start_num=args.start,
        file_type=args.ext
    )