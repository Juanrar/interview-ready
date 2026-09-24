# Code review exercise: find the problems in this code.
# It is intentionally flawed and is not meant to run.

"""
Naming
Privacy
Separation of concerns
Invalid states
Composition (& Delegation) over Inheritance
"""


def code_runner(submission):
    return submission


class Candidate:
    interviews = []
    passed_interview = None
    name = None

    def __init__(self, name):
        self.name = name


class BaseInterview:
    expectation = None
    candidate = None
    submission = None

    def __init__(self, candidate):
        self.candidate = candidate

    def process_submission(self, submission):
        self.submission = submission
        if submission == expectation:
            self.candidate.passed_interview = True


class LiveCodingInterview(BaseInterview):
    def process_submission(self, submission):
        self.submission = submission
        result = self.code_runner()
        if result == self.expectation:
            self.candidate.passed_interview = True

    def code_runner(self):
        return code_runner(self.submission)


cand = Candidate("Gabriel")
interview = LiveCodingInterview(cand)
cand.interviews.append(interview)
interview.process_submission("submission")
assert candidate.passed_interview


# Alternative implementation


class Candidate:  # noqa: F811
    def __init__(self, name):
        self.__interviews = []
        self.name = name

    @property
    def name(self):
        self.__name

    def start_interview(self):
        if self.current_interview():
            raise Exception("Candidate has an active Interview. Do not start a new one")
        interview = LiveCodingInterview()
        self.__interviews.append(interview)

    def submit(self, code):
        self.current_interview.process_submission(code)

    @property
    def interview_status(self):
        self.current_interview.status()

    def current_interview(self):
        return [i for i in self.__interviews if i.status == "pending"][0]


class InterviewStatus:
    def __init__(self, expectation):
        self.__expectation = expectation
        self.__status = "pending"

    def process_results(self, results):
        passed = results == self.__expectation
        self.__status = "passed" if passed else "failed"
        return self.__status


class LiveCodingInterview:  # noqa: F811
    def __init__(self):
        self.__interview_status = InterviewStatus("passed")

    def process_submission(self, submission):
        self.__interview_status.process_results(self.get_results())
        return self.__interview_status.status

    def get_results(self):
        return code_runner(self.submission)

    @property
    def status(self):
        self.__interview_status.status()


candidate = Candidate("Gabriel")
candidate.start_live_coding_interview()
candidate.submit("code")
candidate.get_interview_status()
