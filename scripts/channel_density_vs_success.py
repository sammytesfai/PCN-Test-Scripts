import subprocess
import sys
import json
import time

invoices = ['lntb1m1pjdvaeqpp5d99ghtk7785244efp6frqx76f64e89n7lrtsdhmnw76fxwnllxssdqqcqzzsxq9z0rgqsp5zzwnx4h5dh8360sztw5jarhll9cwzr00w4l9ldp4ec27r2q7m2eq9q8pqqqssqndeawg86p4p4vwccaw0ecns69h56rhgqqarq7xjtr984zt7atwq5avgwtq9k568nyekcajuyvupptnx5d74c2sr4le2ekpd86rq2v9gq6hhuf7', 'lntb1m1pjdvaeqpp5epqqzf3dn6wttz7kpwvuf7hgl2jrervkyvsy7uutdlz45x9kp80sdqqcqzzsxq9z0rgqsp5x37defqqn32xrj0d0mymm0xqk2weerj8fdftmztnwtq0kldj44qq9q8pqqqssq4yekgczwylnwdxxha68dncp03szu24kvu67d3v8tmthvpgzaavfkkpvwh464nurt8fls3wu6dkguzzg43z4f0wrnrxav4y2an7nemzsp9t88sq', 'lntb1m1pjdvaeqpp59g6cfhsr6x5yupkzkn6w8j9wsjqgep3q6njdxeqg2tsxgs78trssdqqcqzzsxq9z0rgqsp5h4wjz9pm3lm73nvvcp7xlyax8ee3a5p6gja5cmf0xmyxchndyxyq9q8pqqqssq8g7saspct4h5t4pqrja3krg6jzu3k4kx7jjzygrj7hp6r83fua9nqleqergzxphlercd3qxhd9f0g2hc2wza8cwu8l6ky49ere5yd6gpdrhqxq', 'lntb1m1pjdvaeqpp58zaqtvztn3s8twdd8rmhprx3gfxz8tu6ld7hqjp6d57dggmhz4fqdqqcqzzsxq9z0rgqsp50etq7s5u94q40f45e5a06kuj6vk0e3atvnr7470gmhzhg6n59xjs9q8pqqqssqr8tlm53875ahg2srsd0zhcjzvuf9n907dkzyergdvvczvyssczezftx8mrwv43jd77v46aj5vmgn6mahta3gksfvkz0nexvd9pgt4hsp3h9eu7', 'lntb1m1pjdvaeqpp5xpuztw3fzsf9yre6sqndlcaf94m2uqshy4p0tqs306tnfnxem0csdqqcqzzsxq9z0rgqsp544p2kgrjjh3gvtuhsw65rc3dlpy52n3x70f9fchefrg4z55qjemq9q8pqqqssq8y3fkd53lhulasfaujr09d9guu4lrkj32lnjxjqu23kmzpe73dlpepemeg3vw4kmjnmsez8e88d79wh9g0zdtxmfwpjld0vnxa3cvpsp5hwnkm', 'lntb1m1pjdvaeqpp5x5m3tx4sds8py9z7lvhq9mc95zqmvhvvpcmy6ywc3sj74857rjysdqqcqzzsxq9z0rgqsp5nnfz98wyp8dgpmshck6xt7rlue594ayrhnr3vpv5h8fhfyge0yyq9q8pqqqssqshcq89h9tzpzjuchhhaewm0sufkjc82lw58ckh9t2qdcxa5zlzlnee25tpzvkq329f2kpa3w7as9gewhfwr7746kysyl8p88quhaxegpt4scpy', 'lntb1m1pjdvaeqpp5fz02n4hu72df620mm424maangpep9pgp98ep2rmcsdv5htsgudjsdqqcqzzsxq9z0rgqsp5fvvg4unw950hc90ja3qpdxm5tx9lujmqvsmmfjfu33wwq9qwrvmq9q8pqqqssqehfan6kyt48qsrtu2h00cl5neugg7wktm7m9rh38tkny8kaenz0qscjz3xgml98eet0pyms6q3k6jmc9kfzpfdwpeu92cllczdlg75gq0xnu6c', 'lntb1m1pjdvaeqpp5avdw3y2gu0fdcjcn6e03tqv4xysx9gqrmedxjudjcx3240w5074sdqqcqzzsxq9z0rgqsp5c2l9arz4qc036jyst9rwqktnc0s4pd7wxwnkgs58halpzxqcy8cs9q8pqqqssqcfedyhjefwrv74jkng4375dwzcycyfydge3kwjqujzxv4n9qpcxxffu03jm0y0sv5fu4a9r2ljwax6hdhnvfv7kkr5wur5d9tal6nhsq633l0e', 'lntb1m1pjdvaeqpp5lttcrnxluvqwajaf550zr5hzfxjfcnfhp73xw6tma3el5hq2pk5sdqqcqzzsxq9z0rgqsp5wjpx4lm4n6thhhmh5ryc6m3jpc7kl6lg7w78hln676yg3wzqjy0q9q8pqqqssqj9jfva6usdhesjnqk257fkxw7w6t49h8zymln8p5pw9kukggymv847qf3gua6wfu22kps23chceqlhpcrhfs4mh8333gjf77kj2jkssqxe6zs9', 'lntb1m1pjdvaeqpp5qz3kj24knsl2wphgywpevcyqj5ex0tkakw5wlcypnz95t3vu0e0qdqqcqzzsxq9z0rgqsp5sdqvgh8hlds7xde8m0yvl2u8u0j24ene7v4wss3hj9qkx689t0ms9q8pqqqssqvkukcgslzyej49z6h83l0pekt0sz94l5e7fmnrn26a5l38lqskhyx78z2ypy5xjkg03kq39509v04e03cqycgl824wpdwph4ht20t0gqp0fxur']
payment_amount = 100000
peer_address = '028970e94cce2d38d707ec4de3da36f1565588ce5f951e0c423a2aea4e1d0631fd'
num_channels = 7

success =0
fail = 0

for i in range(0, len(invoices)):
  print("Successes: {}\nFails: {}".format(success, fail))
  print("Opening Channels:".format(invoices[i]))
  print("")
  output = ''
  error = ''
  for i in range(0, num_channels):
    print("Generating channel {} of amount: {}".format(i+1, 20000))
    result = subprocess.Popen(['lncli','-n', 'testnet', 'openchannel', peer_address, str(20000)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()
    print(output.decode('ascii'))
    print(error.decode('ascii'))
    if len(error.decode('ascii')) > 0:
      break
  if len(error.decode('ascii')) > 0:
    break

  print("")
  print("Waiting for channels to open..")
  print("")
  while(1):
    result = subprocess.run(['lncli', '-n', 'testnet', 'pendingchannels'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    num_pending_channels = len(json.loads(output)['pending_open_channels'])
    if num_pending_channels == 0:
      print("Channels have opened.")
      break

  print("")
  print("Paying Invoice:")
  start_time = time.time()
  result = subprocess.Popen(['lncli','-n', 'testnet', 'payinvoice', invoices[i]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
  result.stdin.write(b'yes\n')
  output, error = result.communicate()
  result.stdin.close()
  print(output.decode('ascii'))
  print(error.decode('ascii'))

  if "SUCCEEDED" not in output.decode('ascii'):
    print("Payment Error:")
    fail += 1
    i -= 1
  else:
    file = open('data/channels_vs_time_fulfill.txt', 'a')
    file.write('{};{}\n'.format(num_channels, time.time()-start_time))
    file.close()
    print("Payment Success:")
    success += 1

  print("")
  print("Closing all open channels...")
  result = subprocess.run(['lncli','-n', 'testnet', 'closeallchannels'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

  while(1):
    result = subprocess.run(['lncli', '-n', 'testnet', 'pendingchannels'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    num_pending_channels = len(json.loads(output)['waiting_close_channels'])
    if num_pending_channels == 0:
      print("Channels have closed.")
      break

  num_channels += 1

print("Success Ratio: {}".format(success/(success+fail)))
