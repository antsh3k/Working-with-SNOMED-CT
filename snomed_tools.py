# Incomplete tool set

class Snomed:
    def __init__(self, input_dict):
        self.snomed2name = input_dict

    def sctid2name(self, sctid):
        return self.snomed2name[sctid][0]

    # def name2sctid(self, name):

    # def sctid2syn

    def sctid2tlc(self, sctid):
        return self.snomed2name[sctid][2]


class Snomed_pt2ch():
    def __init__(self, input_dict):
        self.pt2ch = input_dict

    def get_children(self, sctid):
        """
        Retrieve one layer children terms
        :param sctid: SCTID
        :return: Next level children terms
        """
        return self.pt2ch.get(sctid)

    def get_all_children(self, sctid):
        """
        Get all children of a snomed term
        :param sctid: SCTID
        :return: All snomed children
        """
        result = list()
        stack = [sctid]
        while len(stack) != 0:
            current_snomed = stack.pop()
            current_snomed_parent = self.pt2ch.get(current_snomed, [])
            stack.extend(current_snomed_parent)
            result.append(current_snomed)
            result = list(set(result))
        return result


