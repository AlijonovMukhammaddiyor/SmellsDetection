import cs_designite_runner
import cs_code_split_runner
import cs_learning_data_generator
import tokenizer_runner
import java_designite_runner
import java_codeSplit_runner
import java_learning_data_generator
import os

DATA_BASE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "data",
)

CS_REPO_SOURCE_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "all_cs_repos",
)

BATCH_FILES_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "BatchFiles",
)
CS_SMELLS_RESULTS_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "designite_out",
)
CS_DESIGNITE_CONSOLE_PATH = "C:\\Program Files (x86)\\Designite\\DesigniteConsole.exe"

CS_CODE_SPLIT_OUT_FOLDER_CLASS = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "codesplit_out_class",
)
CS_CODE_SPLIT_OUT_FOLDER_METHOD = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "codesplit_out_method",
)
CS_CODE_SPLIT_MODE_CLASS = "-c"
CS_CODE_SPLIT_MODE_METHOD = "-m"
CS_CODE_SPLIT_EXE_PATH = r"D:\cs454\codeSplit\CodeSplit\bin\Release\CodeSplit.exe"

CS_LEARNING_DATA_FOLDER_BASE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "training_data",
)

TOKENIZER_EXE_PATH = r"D:\cs454\smells\tokenizer\src\tokenizer.exe"
CS_TOKENIZER_OUT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "tokenizer_cs",
)

JAVA_REPO_SOURCE_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "all_java_repos",
)

JAVA_SMELLS_RESULTS_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "designite_out_java",
)
DESIGNITE_JAVA_JAR_PATH = r"D:\cs454\smells\dj\DesigniteJava.jar"

JAVA_CODE_SPLIT_OUT_FOLDER_CLASS = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "codesplit_java_class",
)

JAVA_CODE_SPLIT_OUT_FOLDER_METHOD = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "codesplit_java_method",
)
JAVA_CODE_SPLIT_MODE_CLASS = "class"
JAVA_CODE_SPLIT_MODE_METHOD = "method"
JAVA_CODE_SPLIT_EXE_PATH = r"D:\cs454\smelss\CodeSplitJava\target\CodeSplitJava.jar"

JAVA_LEARNING_DATA_FOLDER_BASE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "smell_data_java",
)

JAVA_TOKENIZER_OUT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "tokenizer_java",
)


if __name__ == "__main__":
    # 1. Run Designite to analyze C# repositories

    cs_designite_runner.analyze_repositories(
        CS_REPO_SOURCE_FOLDER,
        BATCH_FILES_FOLDER,
        CS_SMELLS_RESULTS_FOLDER,
        CS_DESIGNITE_CONSOLE_PATH,
    )

    # 2.1 Run codeSplit to generate class code fragments (each code fragment will contain a class definition)
    cs_code_split_runner.cs_code_split(
        CS_REPO_SOURCE_FOLDER,
        CS_CODE_SPLIT_OUT_FOLDER_CLASS,
        CS_CODE_SPLIT_MODE_CLASS,
        CS_CODE_SPLIT_EXE_PATH,
    )

    # 2.2 Run codeSplit to generate method code fragments (each code fragment will contain a method definition)
    cs_code_split_runner.cs_code_split(
        CS_REPO_SOURCE_FOLDER,
        CS_CODE_SPLIT_OUT_FOLDER_METHOD,
        CS_CODE_SPLIT_MODE_METHOD,
        CS_CODE_SPLIT_EXE_PATH,
    )

    # 3. Run learning data generator that will classify code fragments into either positive or negative cases
    cs_learning_data_generator.generate_data(
        CS_SMELLS_RESULTS_FOLDER,
        CS_CODE_SPLIT_OUT_FOLDER_CLASS,
        CS_CODE_SPLIT_OUT_FOLDER_METHOD,
        CS_LEARNING_DATA_FOLDER_BASE,
    )

    # 4. Run tokenizer to convert code fragments into vectors/matrices of numbers that can be fed to neural network.
    tokenizer_runner.tokenize(
        "CSharp",
        CS_LEARNING_DATA_FOLDER_BASE,
        CS_TOKENIZER_OUT_PATH,
        TOKENIZER_EXE_PATH,
    )

    # 5-8. We repeat the step 1 to 4 for Java repositories
    java_designite_runner.analyze_repositories(
        JAVA_REPO_SOURCE_FOLDER, JAVA_SMELLS_RESULTS_FOLDER, DESIGNITE_JAVA_JAR_PATH
    )

    # 6.1 Run codeSplit to generate class code fragments
    java_codeSplit_runner.java_code_split(
        JAVA_REPO_SOURCE_FOLDER,
        JAVA_CODE_SPLIT_MODE_CLASS,
        JAVA_CODE_SPLIT_OUT_FOLDER_CLASS,
        JAVA_CODE_SPLIT_EXE_PATH,
    )

    # 6.2 Run codeSplit to generate method code fragments
    java_codeSplit_runner.java_code_split(
        JAVA_REPO_SOURCE_FOLDER,
        JAVA_CODE_SPLIT_MODE_METHOD,
        JAVA_CODE_SPLIT_OUT_FOLDER_METHOD,
        JAVA_CODE_SPLIT_EXE_PATH,
    )

    # 7. Run learning data generator that will classify java code fragments into either positive or negative cases
    java_learning_data_generator.generate_data(
        JAVA_SMELLS_RESULTS_FOLDER,
        JAVA_CODE_SPLIT_OUT_FOLDER_CLASS,
        JAVA_CODE_SPLIT_OUT_FOLDER_METHOD,
        JAVA_LEARNING_DATA_FOLDER_BASE,
    )

    # 8. Run tokenizer to convert code fragments into vectors/matrices of numbers that can be fed to neural network.
    tokenizer_runner.tokenize(
        "Java",
        JAVA_LEARNING_DATA_FOLDER_BASE,
        JAVA_TOKENIZER_OUT_PATH,
        TOKENIZER_EXE_PATH,
    )
