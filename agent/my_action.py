from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.context import Context


@AgentServer.custom_action("my_action_111")
class MyCustomAction(CustomAction):

    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> bool:

        print("my_action_111 is running!")

        return True


@AgentServer.custom_action("loop")
class LoopAction(CustomAction):

    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> bool:

        times = argv.param.get("times", 1)
        for i in range(times):
            context.run_task("搜索按钮")
        return True
