class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        unique_email = set()
        for email in emails:
            local, domain = email.split("@")

            local = local.split("+")[0].replace(".", "")

            unique_email.add(f"{local}@{domain}")
        return len(unique_email)


print(
    Solution().numUniqueEmails(
        [
            "fg.r.u.uzj+o.pw@kziczvh.com",
            "r.cyo.g+d.h+b.ja@tgsg.z.com",
            "fg.r.u.uzj+o.f.d@kziczvh.com",
            "r.cyo.g+ng.r.iq@tgsg.z.com",
            "fg.r.u.uzj+lp.k@kziczvh.com",
            "r.cyo.g+n.h.e+n.g@tgsg.z.com",
            "fg.r.u.uzj+k+p.j@kziczvh.com",
            "fg.r.u.uzj+w.y+b@kziczvh.com",
            "r.cyo.g+x+d.c+f.t@tgsg.z.com",
            "r.cyo.g+x+t.y.l.i@tgsg.z.com",
            "r.cyo.g+brxxi@tgsg.z.com",
            "r.cyo.g+z+dr.k.u@tgsg.z.com",
            "r.cyo.g+d+l.c.n+g@tgsg.z.com",
            "fg.r.u.uzj+vq.o@kziczvh.com",
            "fg.r.u.uzj+uzq@kziczvh.com",
            "fg.r.u.uzj+mvz@kziczvh.com",
            "fg.r.u.uzj+taj@kziczvh.com",
            "fg.r.u.uzj+fek@kziczvh.com",
        ]
    )
)
