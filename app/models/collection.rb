class Collection < ApplicationRecord
  has_many :skins, before_add: :get_skin_attributes

  private

  def get_skin_attributes(skin)
    update(category: skin.category, weight_class: skin.weight_class)
  end
end
