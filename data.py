# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home "
#         "to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
#      "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

# question_data = [
#     {
#         "text": "Time on Computers is measured via the EPOX System.",
#         "answer": "False"},
#     {
#         "text": "The Windows 7 operating system has six main editions.",
#         "answer": "True"},
#     {
#         "text": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
#         "answer": "False"},
#     {
#         "text": "Ada Lovelace is often considered the first computer programmer.",
#         "answer": "True"},
#     {
#         "text": "Linux was first created as an alternative to Windows XP.",
#         "answer": "False"},
#     {
#         "text": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
#         "answer": "True"},
#     {
#         "text": "The programming language &quot;Python&quot;"
#                 " is based off a modified version of &quot;JavaScript&quot;.",
#         "answer": "False"},
#     {
#         "text": "The Windows ME operating system was released in the year 2000.",
#         "answer": "True"},
#     {
#         "text": "&quot;HTML&quot; stands for Hypertext Markup Language.",
#         "answer": "True"},
#     {
#         "text": "The logo for Snapchat is a Bell.", "answer": "False"}
# ]
import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

data = response.json()
question_data = data["results"]
