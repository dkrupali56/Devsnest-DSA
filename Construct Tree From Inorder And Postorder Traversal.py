def solve(n1, inorder, n2, postorder):
    has = {el:i for i, el in enumerate(inorder)}

    def get_tree(ps, pe, ins, ine):
        has_idx = has[postorder[ps]]

        l = has_idx - ins
        r = ine - has_idx

        root = TreeNode(postorder[ps])
        root.right = get_tree(ps-1, ps-r, has_idx+1, ine) if r else None
        root.left = get_tree(ps-1-r, pe, ins, has_idx-1) if l else None
        return root

    return get_tree(n2-1, 0, 0, n1-1)
