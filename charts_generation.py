from pyecharts.charts import *
from pyecharts import options as opts

class global_opts:
     def __init__(self) -> None:
          self.opt=False

class bar_generation(global_opts):
    def __init__(self,title:str,x:list,y:list,dataname:str='') -> None:
         super().__init__()
         #后续希望改成链式调用
         self.bar=Bar()
         self.bar.add_xaxis(x)
         self.bar.add_yaxis(dataname,y)
         self.bar.set_global_opts(
              title_opts=opts.TitleOpts(title=title),
          #     toolbox_opts=opts.ToolboxOpts()
         )
         #结果路径
         self.result=self.bar.render('./results/result.html')

class line_generation(global_opts):
     def __init__(self,title:str,x:list,y:list,dataname:str='') -> None:
          super().__init__()
          self.line=Line()
          self.line.add_xaxis(x)
          self.line.add_yaxis(
          series_name=dataname,
          y_axis=y,
          symbol="emptyCircle",
          is_symbol_show=True,
          label_opts=opts.LabelOpts(is_show=True),
          is_connect_nones=True
          )

          self.line.set_global_opts(
          title_opts=opts.TitleOpts(title=title),
          # toolbox_opts=opts.ToolboxOpts(),
          )

          self.result=self.line.render('./results/result.html')


class scatter_generation(global_opts):
     def __init__(self,title:str,x:list,y:list,dataname:str='') -> None:
          super().__init__()
          self.scatter=Scatter()
          self.scatter.add_xaxis(x)
          self.scatter.add_yaxis(dataname,y)
          self.scatter.set_global_opts(
          # toolbox_opts=opts.ToolboxOpts(),
          title_opts=opts.TitleOpts(title=title),
          xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
          yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
          )

          self.result=self.scatter.render('./results/result.html')
           


if __name__=='__main__':
     scatter_generation('水果数量',['香蕉','苹果','梨子','桃子'],[12,34,56,2],'数量')