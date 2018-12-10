from django import forms


class AddArtForm(forms.Form):
    title = forms.CharField(max_length=30, required=True,
                            error_messages={
                                'max_length': '文章标题不能超过30个字符',
                                'required': '文章标题是必填项',
                            })
    category = forms.IntegerField(required=True,
                               error_messages={
                                   'required': '文章栏目是必填项',
                               })
    describe = forms.CharField(max_length=40, required=True,
                           error_messages={
                               'max_length': '文章描述不能超过40个字符',
                               'required': '文章描述是必填项',
                           })
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容是必填项',
                              })
    icon = forms.ImageField(required=True,
                              error_messages={
                                  'required': '文章图片是必填项',
                              })


class UpdateArtForm(forms.Form):
    title = forms.CharField(max_length=30, required=True,
                            error_messages={
                                'max_length': '文章标题不能超过30个字符',
                                'required': '文章标题是必填项',
                            })
    category = forms.IntegerField(required=True,
                                  error_messages={
                                      'required': '文章栏目是必填项',
                                  })
    describe = forms.CharField(max_length=40, required=True,
                               error_messages={
                                   'max_length': '文章描述不能超过40个字符',
                                   'required': '文章描述是必填项',
                               })
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容是必填项',
                              })
    icon = forms.ImageField(required=None)


