/*
    In C#, the System.IO.StreamWriter class is used to write characters to a stream. It provides a convenient way to write text to a file or other output stream.

    To use System.IO.StreamWriter, you first create an instance of the class and pass the path of the file or the output stream you want to write to. You can also specify additional parameters like the encoding to use for the text.
*/
using System.IO;

string filePath = "example.txt";
string textToWrite = "Sanaol";

using (StreamWriter writer = new StreamWriter(filePath))
{
    writer.Write(textToWrite);
}

/*
    In this example, the StreamWriter is created using the file path "example.txt". The using statement ensures that the StreamWriter is properly closed and disposed of when it is no longer needed.

    Once the StreamWriter is created, the Write method is called to write the string "Hello, world!" to the file.

    System.IO.StreamWriter also provides other methods like WriteLine and WriteAsync that can be used to write text to the stream
*/