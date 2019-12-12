class IdConverter:
    """
    GitbucketのユーザIDとBitbucketのユーザIDを変換します
    """

    def __init__(self, mapping: dict):
        self.__mapping = mapping

    def convertToBitbucketId(self, gitbucketId: str) -> str:
        """
        BitbucketのユーザIDに変換します
        IDが存在しない場合はGitbucketのユーザIDをそのまま返します
        """

        trimmed_id = gitbucketId.strip()
        if trimmed_id in self.__mapping:
            return self.__mapping[trimmed_id]

        return trimmed_id
