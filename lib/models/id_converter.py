import yaml


class IdConverter:
    """
    GitbucketのユーザIDとBitbucketのユーザIDを変換します
    """

    def __init__(self, mapping: dict):
        self.__mapping = mapping

    def loadMappingFromFilePath(self, mappingFilePath: str):
        """
        引数に指定されたファイルからマッピングを読み込みます
        """

        with open(mappingFilePath, 'r') as mappingFile:
            self.__mapping = yaml.load(mappingFile)

    def convertToBitbucketId(self, gitbucketId: str) -> str:
        """
        BitbucketのユーザIDに変換します
        IDが存在しない場合はGitbucketのユーザIDをそのまま返します
        """

        trimmed_id = gitbucketId.strip()
        if trimmed_id in self.__mapping:
            return self.__mapping[trimmed_id]

        return trimmed_id
