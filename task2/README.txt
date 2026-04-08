There are some necessary skills for every programmer — process files, calculate checksums, follow the instruction, etc. This task will help to train that.

Use language of your group (C# or Python). In principle, you can use anything else, like Java, PHP, Rust or Ruby or anything you like (you don't submit the code in this task, only the result).

Calculate SHA3-256 for every file from archive. Note, files are binary, you don’t need encodings — if you read file to string with some encoding, you have to use the same encoding to decode string into bytes back for hashing (there is a technical term for such conversions — “stupid activity”).

Write hashes as 64 hex digits in lower case.

Sort hashes in the ascending order of the product of hex digits increased by one (for example, for the hash 63a6ba9e5de66b11ad6c6d3d1b39a5456f65f918fde6250565e365d89a5196c6 the sorting key is 71365623100112242680609229940949951316513259520000000000).

Join sorted hashes without any separator (not keys used for sorting, but hashes themselves).

Concatenate resulted string with your e-mail in lowercase.

Find the SHA3-256 of the result string.