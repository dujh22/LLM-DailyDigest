# GLM4.5本地化部署

官方说明：https://huggingface.co/zai-org/GLM-4.5

下面以8*H800机器为例：

1. 下载：https://modelscope.cn/models/ZhipuAI/GLM-4.5-FP8/summary
2. 根据 `requirements.txt` 安装所需的软件包, 参照：https://github.com/zai-org/GLM-4.5

```shell
pip install -r requirements.txt
```

3. 安装sglang：using pip install sglang from source 参照：https://github.com/sgl-project/sglang

   1. https://docs.sglang.io/get_started/install.html
4. 部署：在使用 `SGLang` 时，发送请求默认会启用思考模式。如果你想禁用思考开关，需要添加 `extra_body={"chat_template_kwargs": {"enable_thinking": False}}` 参数。

   * FP8：
     ```
     python3 -m sglang.launch_server \
       --model-path zai-org/GLM-4.5-FP8 \
       --tp-size 4 \
       --tool-call-parser glm45  \
       --reasoning-parser glm45  \
       --speculative-algorithm EAGLE \
       --speculative-num-steps 3  \
       --speculative-eagle-topk 1  \
       --speculative-num-draft-tokens 4 \
       --mem-fraction-static 0.7 \
       --disable-shared-experts-fusion \
       --served-model-name glm-4.5-fp8 \
       --host 0.0.0.0 \
       --port 8000
     ```
5. 调用：可参考api_request.py
