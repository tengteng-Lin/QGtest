import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess,model_dir='checkpoint/',model_name='run2')

single_text = gpt2.generate(sess, return_as_list=True)[0]
print(single_text)